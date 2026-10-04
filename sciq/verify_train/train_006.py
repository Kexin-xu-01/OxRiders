"""Verification of edits_train/train_006.py.

HISTORY: id -> [(rejected question_adversarial, option picked)], rewritten until IDK won.
MODEL_ANSWERED: rows still answerable after the last rewrite.
"""

HISTORY = {
    "train-00765": [("How many chromosomes are in a particular human cell?", "46 chromosomes")],
    "train-00849": [("How many calories of energy does one gram of a certain nutrient provide?", "4")],
}

MODEL_ANSWERED = {}
