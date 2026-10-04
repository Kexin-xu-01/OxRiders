"""Hand-authored SciQ adversarial edits: validation-00650 .. validation-00779."""

EDITS = {
    # uranus is also featureless in a telescope
    "validation-00665": ("drop_qualifier",
        "What planet looks smooth and featureless through a telescope?"),
    # baryons three, mesons two
    "validation-00669": ("drop_quantifier",
        "What is the term for particles composed of quarks?"),
    "validation-00695": ("drop_list_member",
        "What planet has an upper atmosphere containing ammonia clouds?"),
    "validation-00709": ("generalize_to_category",
        "When was construction of a major american dam completed?"),
    "validation-00727": ("generalize_to_category",
        "Which one of newton's laws describes a relationship involving force?"),
    "validation-00728": ("drop_trailing_condition",
        "The process by which creatures regulate body temperature is known as what?"),
    "validation-00744": ("drop_trailing_condition",
        "What mineral is maintained at normal levels in blood?"),
    "validation-00752": ("drop_list_member",
        "Which joint allows humans to pivot?"),
    # sporophyte meiosis, gametophyte mitosis
    "validation-00765": ("generalize_to_category",
        "A plant generation produces its reproductive cells by what process?"),
    "validation-00766": ("exchange_feature",
        "What type of covalent bond depends on how the bonding electrons are shared between the two atoms?"),
    "validation-00769": ("drop_quantifier",
        "Comets that have periods of a certain length are knows as what-period comets?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_TRUNC = "question text truncated in source"
_reasons = {
    _NONSENSE: [657, 662, 672, 673, 674, 678, 687, 691, 696, 701, 716, 726, 735,
                737, 742, 751, 757, 758, 763, 777],
    _OVERLAP: [650, 666, 668, 681, 686, 718, 732, 762, 767, 770],
    _CONTEST: [655, 661, 670, 690, 692, 698, 700, 706, 708, 720, 730, 746, 747],
    _TRUNC: [680],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(650, 780)
    if f"validation-{n:05d}" not in EDITS
}
