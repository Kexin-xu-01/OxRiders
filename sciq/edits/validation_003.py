"""Hand-authored SciQ adversarial edits: validation-00260 .. validation-00389."""

EDITS = {
    "validation-00273": ("drop_trailing_condition",
        "Which process helps microorganisms make food?"),
    "validation-00276": ("drop_trailing_condition",
        "What kind of mixture is formed when two substances are combined?"),
    # cars use catalytic converters, smokestacks scrubbers
    "validation-00279": ("generalize_to_category",
        "What do machines use to remove pollutants from exhaust before releasing it?"),
    "validation-00280": ("generalize_to_category",
        "Organisms of a species typically have how many pairs of chromosomes?"),
    "validation-00288": ("drop_list_member",
        "Name the white blood cells that can squeeze through capillary walls."),
    "validation-00294": ("drop_qualifier",
        "In projectile motion, the displacement of an object along one axis is called its what?"),
    "validation-00304": ("exchange_feature",
        "What are cyclic compounds called, depending on which atoms are in the ring?"),
    # megaspores -> female, microspores -> male
    "validation-00305": ("drop_qualifier",
        "Surviving spores develop into what?"),
    "validation-00319": ("drop_qualifier",
        "What is a developing baby in the uterus called?"),
    "validation-00329": ("drop_superlative",
        "What is considered to be a common igneous rock?"),
    "validation-00354": ("drop_quantifier",
        "What type of event often occurs at plate boundaries?"),
    "validation-00389": ("drop_trailing_condition",
        "Touching, coughing, or sneezing are examples of directly spreading what microorganisms?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [264, 266, 268, 277, 278, 284, 285, 298, 303, 307, 312, 339, 344,
                346, 358, 366, 367, 370, 372, 377, 379, 380, 381, 383],
    _OVERLAP: [272, 287, 320, 371, 388],
    _CONTEST: [271, 274, 290, 291, 292, 296, 297, 311, 318, 331, 332, 368],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(260, 390)
    if f"validation-{n:05d}" not in EDITS
}
