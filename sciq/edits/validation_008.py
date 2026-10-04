"""Hand-authored SciQ adversarial edits: validation-00890 .. validation-00999."""

EDITS = {
    "validation-00901": ("exchange_feature",
        "What is the form of logical thinking that relates observations and general conclusions called?"),
    # NH: east-deflected poleward flow; equatorward flow deflected west
    "validation-00903": ("merge_alternatives",
        "Wind or water that travels between the poles and the equator curves in which direction?"),
    "validation-00912": ("drop_superlative",
        "What is an element in organic compounds?"),
    "validation-00925": ("drop_trailing_condition",
        "What is a short band of tough connective tissue that attaches to bones?"),
    "validation-00926": ("drop_trailing_condition",
        "When you change a material, what is this change known as?"),
    "validation-00928": ("drop_qualifier",
        "What is part of the moon's shadow called?"),
    "validation-00937": ("drop_superlative",
        "Which element has a high electronegativity value?"),
    "validation-00954": ("generalize_to_category",
        "A body of water is an example of h20 in which state of matter?"),
    # larvae bilateral, adults radial
    "validation-00960": ("drop_qualifier",
        "What kind of symmetry do echinoderms possess?"),
    "validation-00962": ("drop_qualifier",
        "Fires, caused by what, are a disturbance in temperate grasslands?"),
    "validation-00983": ("drop_qualifier",
        "Receptors for which hormones reside in a specific location in the cell?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_TRUNC = "question text truncated in source"
_reasons = {
    _NONSENSE: [896, 909, 915, 932, 949, 953, 958, 961, 978, 986],
    _OVERLAP: [898, 911, 913, 917, 940, 945, 950, 956, 984, 987],
    _CONTEST: [929, 933, 943, 955, 968, 973, 976, 977, 999],
    _TRUNC: [991],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(890, 1000)
    if f"validation-{n:05d}" not in EDITS
}
