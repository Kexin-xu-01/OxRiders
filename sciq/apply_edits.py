"""Merge every edits/*.py batch into sciq-all.csv and write the adversarial files.

Outputs
  sciq-adversarial.csv          all 13679 rows; authored rows have question_adversarial
  sciq-adversarial-authored.csv authored rows that passed both filters
                                (still_answerable.py, model_answered.py)

Each row is a matched pair over ONE shared option pool (same design as the
LAB-Bench LitQA2 + SuppQA cut, see ../add_idk_option.py):

  question              -> answer              (original key)
  question_adversarial  -> answer_adversarial  ("I don't know")

Pool = answer + distractor_1..4. SciQ always has exactly three distractors, so
"first free slot" would put "I don't know" in distractor_4 on every row -- a
positional cue. Instead its slot is chosen per row from a hash of the id.
Shuffle the pool at training time regardless.
"""

import csv
import glob
import hashlib
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from still_answerable import STILL_ANSWERABLE  # noqa: E402
from model_answered import MODEL_ANSWERED  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "sciq-all.csv")
OUT_ALL = os.path.join(ROOT, "sciq-adversarial.csv")
OUT_CUT = os.path.join(ROOT, "sciq-adversarial-authored.csv")
IDK = "I don't know"

CATEGORY = {
    "generalize_to_category": "remove_name",
    "drop_antecedent": "remove_name",
    "drop_qualifier": "remove_condition",
    "drop_trailing_condition": "remove_condition",
    "drop_quantifier": "remove_condition",
    "drop_superlative": "remove_condition",
    "drop_list_member": "remove_condition",
    "drop_comparator": "remove_condition",
    "exchange_feature": "exchange_concept",
    "merge_alternatives": "exchange_concept",
}

FIELDS = (["split", "id", "adversarial_category", "adversarial_mechanism",
           "question", "question_adversarial", "answer", "answer_adversarial"]
          + [f"distractor_{i}" for i in range(1, 5)]
          + ["generated_by", "needs_review", "review_class", "review_reason",
             "batch", "support"])


TRAIN_DEFAULT_FLAG = "no edit leaves two or more options fitting"


def load_module(path):
    name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return name, mod


def load_batches(all_ids):
    """edits/*.py list FLAGGED explicitly; edits_train/*.py give a REVIEWED id range
    and every reviewed row without an EDIT is flagged with TRAIN_DEFAULT_FLAG."""
    edits, flagged = {}, {}
    paths = (sorted(glob.glob(os.path.join(ROOT, "edits", "*.py")))
             + sorted(glob.glob(os.path.join(ROOT, "edits_train", "*.py"))))
    for path in paths:
        name, mod = load_module(path)
        reviewed = getattr(mod, "REVIEWED", None)
        if reviewed:
            lo, hi = reviewed
            implicit = {i: TRAIN_DEFAULT_FLAG for i in all_ids
                        if i.split("-")[0] == lo.split("-")[0] and lo <= i <= hi}
            assert set(mod.EDITS) <= set(implicit), f"{name}: EDITS outside REVIEWED"
            mod.FLAGGED = {k: v for k, v in implicit.items() if k not in mod.EDITS}
        for k, v in getattr(mod, "EDITS", {}).items():
            assert k not in edits and k not in flagged, f"{k} appears twice ({name})"
            edits[k] = (*v, name)
        for k, v in getattr(mod, "FLAGGED", {}).items():
            assert k not in edits and k not in flagged, f"{k} appears twice ({name})"
            flagged[k] = (v, name)
    return edits, flagged


def load_verify():
    """verify_train/*.py: MODEL_ANSWERED dicts from the per-batch verification pass."""
    out = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "verify_train", "*.py"))):
        name, mod = load_module(path)
        for k, v in mod.MODEL_ANSWERED.items():
            assert k not in out and k not in MODEL_ANSWERED, f"{k} twice ({name})"
            out[k] = v
    return out


def idk_slot(row_id):
    return int(hashlib.sha1(row_id.encode()).hexdigest(), 16) % 4


with open(SRC, newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))
ids = {r["id"] for r in rows}
edits, flagged = load_batches(sorted(ids))
MODEL_ANSWERED = {**MODEL_ANSWERED, **load_verify()}
missing = sorted((set(edits) | set(flagged)) - ids)
assert set(STILL_ANSWERABLE) <= set(edits), sorted(set(STILL_ANSWERABLE) - set(edits))
assert set(MODEL_ANSWERED) <= set(edits), sorted(set(MODEL_ANSWERED) - set(edits))
assert not set(STILL_ANSWERABLE) & set(MODEL_ANSWERED)
assert not missing, f"unknown ids: {missing[:10]}"

out, cut = [], []
for r in rows:
    dist = [r["distractor_1"], r["distractor_2"], r["distractor_3"]]
    pool = [r["answer"]] + dist
    assert not any(IDK.lower() in o.lower() for o in pool), r["id"]
    dist.insert(idk_slot(r["id"]), IDK)
    o = {k: "" for k in FIELDS}
    o.update(split=r["split"], id=r["id"], question=r["question"],
             answer=r["answer"], support=r["support"])
    for i, d in enumerate(dist, 1):
        o[f"distractor_{i}"] = d

    if r["id"] in edits:
        mech, newq, batch = edits[r["id"]]
        assert mech in CATEGORY, f"{r['id']}: unknown mechanism {mech}"
        assert newq.strip() and newq.strip().lower() != r["question"].strip().lower(), r["id"]
        o.update(question_adversarial=newq, answer_adversarial=IDK,
                 adversarial_mechanism=mech, adversarial_category=CATEGORY[mech],
                 generated_by="manual", batch=batch)
        if r["id"] in STILL_ANSWERABLE:
            o.update(answer_adversarial="", needs_review="yes",
                     review_class="still_answerable",
                     review_reason=STILL_ANSWERABLE[r["id"]])
        elif r["id"] in MODEL_ANSWERED:
            o.update(answer_adversarial="", needs_review="yes",
                     review_class="model_answered",
                     review_reason=f"model picked: {MODEL_ANSWERED[r['id']]}")
        else:
            cut.append(o)
    elif r["id"] in flagged:
        reason, batch = flagged[r["id"]]
        o.update(needs_review="yes", review_class="D", review_reason=reason, batch=batch)
    out.append(o)

for path, data in ((OUT_ALL, out), (OUT_CUT, cut)):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(data)

by_split = {}
for o in cut:
    by_split[o["split"]] = by_split.get(o["split"], 0) + 1
print(f"authored: {len(edits)}  still answerable: {len(STILL_ANSWERABLE)}  "
      f"model answered: {len(MODEL_ANSWERED)}  "
      f"kept: {len(cut)}  flagged: {len(flagged)}  by split: {by_split}")
print(f"wrote {OUT_ALL}\nwrote {OUT_CUT}")
