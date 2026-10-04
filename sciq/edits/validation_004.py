"""Hand-authored SciQ adversarial edits: validation-00390 .. validation-00519."""

EDITS = {
    "validation-00390": ("drop_qualifier",
        "Which blood pressure is recorded during one phase of the cardiac cycle?"),
    "validation-00402": ("drop_superlative",
        "What is a large known animal?"),
    "validation-00404": ("generalize_to_category",
        "A european wildflower was introduced to which continent in the 1800's?"),
    "validation-00417": ("drop_superlative",
        "What are an abundant source of energy found in foods?"),
    # prefrontal: working, amygdala: emotional, cerebellum: procedural
    "validation-00422": ("generalize_to_category",
        "Which part of the brain is responsible for a type of memory?"),
    "validation-00435": ("drop_quantifier",
        "A carbon atom with 6 protons and several neutrons is more specifically known as?"),
    "validation-00438": ("generalize_to_category",
        "What is the result of a reaction between a nonmetal oxide and water?"),
    "validation-00452": ("drop_trailing_condition",
        "The main function of this organ is to filter the blood?"),
    "validation-00497": ("drop_qualifier",
        "How do seismologists measure the intensity of an earthquake?"),
    # lowers freezing point, raises boiling point
    "validation-00504": ("merge_alternatives",
        "What does antifreeze do to the freezing or boiling point of coolant?"),
    "validation-00515": ("drop_quantifier",
        "What is the name for groups of stars?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [397, 400, 405, 409, 415, 419, 420, 423, 427, 432, 439, 440, 443,
                444, 451, 453, 463, 471, 480, 486, 487, 495, 503, 505, 506, 514,
                518],
    _OVERLAP: [401, 411, 442, 469, 475, 498, 507, 508, 510, 519],
    _CONTEST: [399, 410, 418, 426, 429, 454, 468, 476],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(390, 520)
    if f"validation-{n:05d}" not in EDITS
}
