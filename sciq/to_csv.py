"""Flatten allenai/sciq (train/validation/test parquet) into one CSV.

- SciQ has no row id, so `id` = `<split>-<row index>` (e.g. `test-00042`), stable
  as long as the upstream parquet files are unchanged.
- `correct_answer` -> `answer`; `distractor1..3` -> `distractor_1..3`.
- `support` is the passage SciQ ships with ~89% of rows (blank otherwise).

Re-fetch the source with:
    from huggingface_hub import snapshot_download
    snapshot_download("allenai/sciq", repo_type="dataset", local_dir=".")
then move data/*.parquet next to this script.
"""

import csv
import os
import pyarrow.parquet as pq

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "sciq-all.csv")
SPLITS = ["train", "validation", "test"]
COLUMNS = ["split", "id", "question", "answer",
           "distractor_1", "distractor_2", "distractor_3", "support"]


def find(split):
    for cand in (f"{split}-00000-of-00001.parquet",
                 os.path.join("data", f"{split}-00000-of-00001.parquet"),
                 f"{split}.parquet"):
        p = os.path.join(ROOT, cand)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"no parquet for split {split!r} under {ROOT}")


n = 0
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=COLUMNS)
    w.writeheader()
    for split in SPLITS:
        rows = pq.read_table(find(split)).to_pylist()
        for i, r in enumerate(rows):
            w.writerow({
                "split": split,
                "id": f"{split}-{i:05d}",
                "question": r["question"],
                "answer": r["correct_answer"],
                "distractor_1": r["distractor1"],
                "distractor_2": r["distractor2"],
                "distractor_3": r["distractor3"],
                "support": r["support"],
            })
            n += 1
        print(f"{split:<11} {len(rows):>6}")
print(f"wrote {n} rows -> {OUT}")
