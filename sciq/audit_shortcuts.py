"""Surface-form leakage audit for the SciQ adversarial pairs.

Paired probe: positives are question_adversarial, negatives are the ORIGINAL
question of the same rows. Folds are grouped by row so both versions of a row
land in the same fold. Effective AUC = max(auc, 1-auc).

Reports length AUC, bag-of-words NB AUC, per-mechanism mean char delta and the
most one-sided tokens (the kind of tell `this` was in the LAB-Bench audit).
Pure stdlib, same probes as ../scripts/audit_shortcuts.py.
"""

import csv
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "sciq-adversarial-authored.csv")
WORD = re.compile(r"[a-z0-9_\-']+")


def auc(scores, labels):
    pairs = sorted(zip(scores, labels))
    rsum, i, npos = 0.0, 0, sum(labels)
    nneg = len(labels) - npos
    while i < len(pairs):
        j = i
        while j + 1 < len(pairs) and pairs[j + 1][0] == pairs[i][0]:
            j += 1
        avg = (i + j) / 2 + 1
        rsum += avg * sum(1 for k in range(i, j + 1) if pairs[k][1] == 1)
        i = j + 1
    return (rsum - npos * (npos + 1) / 2) / (npos * nneg)


def eff(a):
    return max(a, 1 - a)


def tokens(t):
    return WORD.findall(t.lower())


def nb_cv(texts, labels, groups, folds=5, seed=7):
    g = sorted(set(groups))
    random.Random(seed).shuffle(g)
    fold_of = {x: i % folds for i, x in enumerate(g)}
    scores = [0.0] * len(texts)
    for f in range(folds):
        cnt, tot = [Counter(), Counter()], [0, 0]
        for i, t in enumerate(texts):
            if fold_of[groups[i]] != f:
                tk = tokens(t)
                cnt[labels[i]].update(tk)
                tot[labels[i]] += len(tk)
        V = len(set(cnt[0]) | set(cnt[1])) or 1
        for i, t in enumerate(texts):
            if fold_of[groups[i]] == f:
                scores[i] = sum(math.log((cnt[1][w] + 1) / (tot[1] + V))
                                - math.log((cnt[0][w] + 1) / (tot[0] + V))
                                for w in tokens(t) if w in cnt[0] or w in cnt[1])
    return auc(scores, labels)


rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else SRC, encoding="utf-8")))
texts, labels, groups = [], [], []
for r in rows:
    texts += [r["question_adversarial"], r["question"]]
    labels += [1, 0]
    groups += [r["id"], r["id"]]

print(f"paired probe set: {len(rows)} rows\n")
print(f"  length AUC (eff)        {eff(auc([float(len(t)) for t in texts], labels)):.3f}")
print(f"  bag-of-words NB (eff)   {eff(nb_cv(texts, labels, groups)):.3f}")

agg = defaultdict(list)
for r in rows:
    agg[r["adversarial_mechanism"]].append(len(r["question_adversarial"]) - len(r["question"]))
print("\nper-mechanism mean char delta:")
for m, ds in sorted(agg.items(), key=lambda kv: -len(kv[1])):
    print(f"  {m:28} {sum(ds)/len(ds):7.1f}  n={len(ds)}")

df = [Counter(), Counter()]
for t, y in zip(texts, labels):
    df[y].update(set(tokens(t)))
skew = sorted(set(df[0]) | set(df[1]),
              key=lambda w: -abs(df[1][w] - df[0][w]))
print("\nmost one-sided tokens (unanswerable : answerable doc counts):")
for w in skew[:15]:
    print(f"  {w:18} {df[1][w]:5} : {df[0][w]}")
