"""Merge every edits/*.py batch into sciq-all.csv and write the adversarial files.

Outputs
  sciq-adversarial.csv          all 13679 rows; authored rows have question_adversarial
  sciq-adversarial-authored.csv authored rows that passed the self-answer filter
                                (still_answerable.py)

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


def load_batches():
    edits, flagged = {}, {}
    for path in sorted(glob.glob(os.path.join(ROOT, "edits", "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for k, v in getattr(mod, "EDITS", {}).items():
            assert k not in edits and k not in flagged, f"{k} appears twice ({name})"
            edits[k] = (*v, name)
        for k, v in getattr(mod, "FLAGGED", {}).items():
            assert k not in edits and k not in flagged, f"{k} appears twice ({name})"
            flagged[k] = (v, name)
    return edits, flagged


def idk_slot(row_id):
    return int(hashlib.sha1(row_id.encode()).hexdigest(), 16) % 4


edits, flagged = load_batches()
with open(SRC, newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh))
ids = {r["id"] for r in rows}
missing = sorted((set(edits) | set(flagged)) - ids)
assert set(STILL_ANSWERABLE) <= set(edits), sorted(set(STILL_ANSWERABLE) - set(edits))
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
      f"kept: {len(cut)}  flagged: {len(flagged)}  by split: {by_split}")
print(f"wrote {OUT_ALL}\nwrote {OUT_CUT}")
