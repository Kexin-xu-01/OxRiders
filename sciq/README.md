# SciQ "I don't know" adversarial set

Unanswerable variants of [allenai/sciq](https://huggingface.co/datasets/allenai/sciq)
(CC BY-NC 3.0), built the same way as the LAB-Bench set in the repo root: each
authored row pairs the original `question` with a `question_adversarial` that
removes or alters the information needed to pick a unique option. Both share one
option pool, which also contains `"I don't know"`; the adversarial key is
`"I don't know"`.

## Impossible-premise set (`sciq-impossible*.csv`)

Every one of the 13,679 SciQ rows (train 11,679, validation 1,000, test 1,000) has a
hand-written `question_adversarial` that keeps the original question and adds a condition that
makes no biological or physical sense, so no option can be correct. Examples:

- "Vertebrata living inside the core of the sun are characterized by the presence of what?"
- "What are the two most common silicates that contain no silicon?"
- "In a universe with no atoms, no protons, no electric charge, no nuclei, no particles and no matter, what part of an atom is positive due to the presence of positively charged protons?"

The original `answer` and all three distractors are kept, `"I don't know"` is added in a slot
chosen by a hash of the row id, and `answer_adversarial` is `"I don't know"`
(`adversarial_mechanism=add_impossible_condition`, `adversarial_category=impossible_premise`).

| file | what |
|---|---|
| `edits_impossible/*.py` | `REVIEWED` id range + `EDITS` (`id -> question_adversarial`), 100 rows per module |
| `apply_impossible.py` | checks each module covers its range exactly with no overlap, and that every rewrite is non-empty and differs from the original; writes the two CSVs |
| `sciq-impossible.csv` | all 13,679 rows |
| `sciq-impossible-authored.csv` | authored rows only (also 13,679; none flagged) |

Checks run on the final files: 13,679 unique ids; question, answer and the three distractors
match `sciq-all.csv` for every row; exactly one `"I don't know"` per row, spread evenly over the
four slots (3,402 / 3,403 / 3,457 / 3,417); no empty or unchanged rewrite.

Verification: rewrites were written and checked by one model (the author). No GPT, Claude or
Gemini calls were made (no API keys were available), so there is no multi-model consensus.

Shortcut audit (paired original vs rewrite, logistic regression, 5-fold CV grouped by id):

| probe | AUC |
|---|---|
| length (words) | 0.94 |
| bag-of-words | 1.00 (0.997) |

Rewrites average 26.1 words against 12.9 for the originals. The word "no" appears in 90% of
rewrites and 0.4% of originals; "with no" is in 79%, "in a universe" in 32%, "on a planet" in 26%,
"where nothing" in 19%. A text classifier can therefore tell rewrites from originals almost
perfectly without any science. Use this set to test whether a model notices an impossible premise
and abstains, not as a shortcut-free benchmark. Some source questions carry SciQ's own typos or
questionable keys; rewrites keep the source wording as is.

Reproduce: `python3 apply_impossible.py`.

The sections below describe the earlier underdetermined set (`sciq-adversarial*.csv`), kept for
reference.

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
| train | 11679 | 2046 | 13 | 0 | 9633 |
| total | 13679 | 2394 | 185 | 2 | 11283 |

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
Train (all 11,679 rows, 116 batches in `edits_train/`) follows the same loop: `verify_train/*.py`
records any rewrite that was answered; all 13 train rewrites ended on "I don't know".

## Mechanisms

New SciQ-specific mechanisms, mapped onto the canonical categories in `apply_edits.CATEGORY`:
`generalize_to_category`, `drop_qualifier`, `drop_trailing_condition`, `drop_quantifier`,
`drop_superlative`, `drop_list_member`, `drop_antecedent`, `exchange_feature`,
`merge_alternatives`.

Example (`test-00600`): "Most hydrogen atoms have how many protons?" becomes
"Most atoms have how many protons?"

## Shortcut audit

On all 2394 kept pairs, length gives a classifier 0.53 AUC and bag-of-words gives 0.98.
The bag-of-words leak comes from the edit wording: vague references ("a particular",
"a certain", "a given", "a specific") appear in about 2250 adversarial questions and almost
never in the originals. Rotating four phrasings does not help, since every one of them is a giveaway.
Treat this as a known bias when evaluating.

## Reproduce

```bash
# parquet files from the HF repo go in sciq/ (ignored by git)
python3 to_csv.py
python3 apply_edits.py
python3 audit_shortcuts.py
```
