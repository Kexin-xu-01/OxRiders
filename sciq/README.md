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
| `still_answerable.py` | self-answer filter: authored edits that could still be answered from the options, with the winning option |
| `apply_edits.py` | merges all batches into `sciq-adversarial.csv` (every row) and `sciq-adversarial-authored.csv` (authored rows that pass the filter) |
| `audit_shortcuts.py` | paired length / bag-of-words probes, grouped CV by id (adapted from `../audit_shortcuts.py`) |

`"I don't know"` is inserted into a distractor slot chosen by a hash of the row id,
so its position does not leak the class.

## Coverage

| split | rows | kept | still answerable | flagged |
|---|---|---|---|---|
| test | 1000 | 220 | 32 | 748 |
| validation | 1000 | 86 | 12 | 902 |
| train | 11679 | 0 | - | not reviewed |

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

## Mechanisms

New SciQ-specific mechanisms, mapped onto the canonical categories in `apply_edits.CATEGORY`:
`generalize_to_category`, `drop_qualifier`, `drop_trailing_condition`, `drop_quantifier`,
`drop_superlative`, `drop_list_member`, `drop_antecedent`, `exchange_feature`,
`merge_alternatives`.

Example (`test-00600`): "Most hydrogen atoms have how many protons?" becomes
"Most atoms have how many protons?"

## Shortcut audit

On the 306 kept pairs, length gives a classifier 0.62 AUC and bag-of-words gives 0.70.
The edits mostly shorten questions and swap specific nouns for generic ones, which accounts for both numbers.
Treat this as a known bias when evaluating.

## Reproduce

```bash
# parquet files from the HF repo go in sciq/ (ignored by git)
python3 to_csv.py
python3 apply_edits.py
python3 audit_shortcuts.py
```
