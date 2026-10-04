# SciQ "I don't know" adversarial set

Unanswerable variants of [allenai/sciq](https://huggingface.co/datasets/allenai/sciq)
(CC BY-NC 3.0), built the same way as the LAB-Bench set in the repo root: each
authored row pairs the original `question` with a `question_adversarial` that
removes or alters the information needed to pick a unique option. Both share one
option pool, which also contains `"I don't know"`; the adversarial key is
`"I don't know"`.

## Files

| file | what |
|---|---|
| `to_csv.py` | flattens the three SciQ parquet splits into `sciq-all.csv` with stable ids `<split>-<index>` |
| `edits/*.py` | hand-authored `EDITS` (`id -> (mechanism, question_adversarial)`) and `FLAGGED` (`id -> reason`) per batch |
| `still_answerable.py` | filter 1: authored edits that could still be answered from the options, with the winning option |
| `model_answered.py` | filter 2: rows where the model, offered all 5 options, picked a real answer over "I don't know" |
| `regen.py` | rewrites of every row dropped by filters 1–2, each re-answered blind until "I don't know" won (max 3 rounds) |
| `edits_train/*.py` | train batches: `REVIEWED` id range + `EDITS`; reviewed rows without an edit are flagged |
| `verify_train/*.py` | per-batch verification: `HISTORY` (rejected rewrites + option picked) and `MODEL_ANSWERED` |
| `apply_edits.py` | merges all batches into `sciq-adversarial.csv` (every row) and `sciq-adversarial-authored.csv` (authored rows that pass both filters) |
| `audit_shortcuts.py` | paired length / bag-of-words probes, grouped CV by id (adapted from `../audit_shortcuts.py`) |

`"I don't know"` is inserted into a distractor slot chosen by a hash of the row id,
so its position does not leak the class.

## Coverage

| split | rows | kept | regenerated | regen exhausted | flagged |
|---|---|---|---|---|---|
| test | 1000 | 250 | 130 | 2 | 748 |
| validation | 1000 | 98 | 42 | 0 | 902 |
| train | 11679 | in progress (batched, see `edits_train/`) | | | |

Every test and validation row was read by hand. A row is authored only if, after the
edit, at least two of the four original options fit (or none can be selected).
SciQ answers are often common knowledge, so dropping words alone is not enough. The edit has to
remove the cue that singles out the key. Rows are flagged rather than forced when:

- only one option is plausible under any edit (most flags),
- the distractors are nonsense,
- the original key is contestable,
- options overlap or are near-synonyms,
- the source question is truncated.

Self-answer filter: every authored `question_adversarial` was then answered blind from its
option pool. The 44 that could still be answered with confidence are listed in
`still_answerable.py` and dropped from `sciq-adversarial-authored.csv`. They stay in
`sciq-adversarial.csv` with `needs_review=yes`, `review_class=still_answerable`, and an
empty `answer_adversarial`.

Model-answer filter (stricter): the rest were answered again with all 5 options shuffled,
"I don't know" included. A real option was picked whenever one looked more likely than the
others, or whenever the question asks for any example and several options are valid ("What is
a common STI?"). Only rows where "I don't know" won are kept. The other 128 are in
`model_answered.py` (`review_class=model_answered`). The authoring model made this call
itself. Other models were not queried.

Regeneration: the 172 rows dropped by the two filters were not discarded. Each was rewritten
(usually by replacing the identifying detail with "a certain / given / specific / particular X"
so that two or more options fit) and answered again blind with shuffled options. If a real option
still won, it was rewritten again, up to 3 rounds (`regen.py` keeps every attempt and the option
picked). 170 now end on "I don't know". 2 were still answerable after 3 rewrites and are kept in
the full CSV as `review_class=regen_exhausted`. `regen_rounds` counts rejected rewrites per row.
Train batches follow the same loop: `verify_train/*.py` records any rewrite that was answered.

## Mechanisms

New SciQ-specific mechanisms, mapped onto the canonical categories in `apply_edits.CATEGORY`:
`generalize_to_category`, `drop_qualifier`, `drop_trailing_condition`, `drop_quantifier`,
`drop_superlative`, `drop_list_member`, `drop_antecedent`, `exchange_feature`,
`merge_alternatives`.

Example (`test-00600`): "Most hydrogen atoms have how many protons?" becomes
"Most atoms have how many protons?"

## Shortcut audit

On the 366 kept pairs, length gives a classifier 0.56 AUC and bag-of-words gives 0.85.
The bag-of-words leak comes from the regeneration wording: vague references ("a certain",
"a given", "a specific", "a particular") never occur in the originals. They are rotated across
four phrasings, but a classifier still keys on them.
Treat this as a known bias when evaluating.

## Reproduce

```bash
# parquet files from the HF repo go in sciq/ (ignored by git)
python3 to_csv.py
python3 apply_edits.py
python3 audit_shortcuts.py
```
