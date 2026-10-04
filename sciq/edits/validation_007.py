"""Hand-authored SciQ adversarial edits: validation-00780 .. validation-00889."""

EDITS = {
    "validation-00783": ("drop_superlative",
        "What is an important element to life?"),
    # network covalent solids melt high, molecular covalent solids low
    "validation-00816": ("drop_qualifier",
        "At what temperatures do crystals formed by covalent solids melt at?"),
    "validation-00835": ("generalize_to_category",
        "Regular checkups with what type of specialist can detect cancers early?"),
    "validation-00836": ("drop_qualifier",
        "Receptors for what sense are located within sensory hairs on insects?"),
    "validation-00846": ("generalize_to_category",
        "What is the cartilaginous structure of the airway?"),
    "validation-00854": ("drop_superlative",
        "What is a common cause of hearing loss?"),
    "validation-00866": ("exchange_feature",
        "If the area to which a force is applied is changed, then the pressure will be?"),
    # cardiac cells also usually have one nucleus
    "validation-00870": ("drop_list_member",
        "What kind of muscle cells have a single nucleus?"),
    "validation-00874": ("exchange_feature",
        "What are trees called based on whether they lose their leaves during winter?"),
    "validation-00875": ("drop_qualifier",
        "Normal human cells have a total of how many chromosomes per cell?"),
    "validation-00881": ("exchange_feature",
        "What type of evolution happens when the traits of two species change relative to each other?"),
    "validation-00883": ("drop_trailing_condition",
        "What is the principal blood vessel through which blood leaves the heart?"),
    "validation-00889": ("exchange_feature",
        "At what temperatures do alkanes with a different number of carbon atoms boil?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [781, 782, 787, 807, 811, 824, 827, 852, 857, 878, 884, 885, 886,
                888],
    _OVERLAP: [805, 820, 860],
    _CONTEST: [784, 795, 796, 799, 812, 823, 840, 844, 862],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(780, 890)
    if f"validation-{n:05d}" not in EDITS
}
