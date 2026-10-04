"""Verification of edits_train/train_004.py.

HISTORY: id -> [(rejected question_adversarial, option picked)], rewritten until IDK won.
MODEL_ANSWERED: rows still answerable after the last rewrite.
"""

HISTORY = {
    "train-00500": [("The products of a particular reaction are glucose and what else?", "oxygen")],
    "train-00565": [("How many different kinds of ions are produced when a certain salt dissociates?", "two")],
    "train-00594": [("The complete hydrolysis of a given carbohydrate yields what?", "glucose")],
}

MODEL_ANSWERED = {}
