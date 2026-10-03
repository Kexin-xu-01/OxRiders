"""Hand-authored SciQ adversarial edits: validation-00130 .. validation-00259."""

EDITS = {
    "validation-00146": ("generalize_to_category",
        "Changes in behavior and physiology are methods mammals use for what purpose?"),
    "validation-00148": ("drop_qualifier",
        "Unsaturated hydrocarbons with at least one multiple bond are known as?"),
    "validation-00160": ("drop_qualifier",
        "Which biological system is responsible for getting rid of waste?"),
    "validation-00163": ("generalize_to_category",
        "What kind of light bulb is commonly used in homes?"),
    "validation-00164": ("drop_qualifier",
        "What is the name for the circle that serves as a reference line for map coordinates?"),
    "validation-00173": ("drop_quantifier",
        "When a binary acid has a certain number of acidic hydrogens, what is it known as?"),
    "validation-00182": ("drop_qualifier",
        "Cellular respiration that proceeds under certain oxygen conditions is called what?"),
    "validation-00191": ("generalize_to_category",
        "How do worms reproduce?"),
    # intraspecific vs interspecific
    "validation-00192": ("drop_qualifier",
        "Competition can occur between members of the same what?"),
    # grebes have lobed feet, gulls and ducks webbed
    "validation-00202": ("drop_qualifier",
        "Some birds have what type of feet used for swimming or floating?"),
    # Betelgeuse red, Rigel blue
    "validation-00216": ("generalize_to_category",
        "A bright star in Orion is an example of what \"colorful\" stage in the life of very massive stars?"),
    "validation-00244": ("generalize_to_category",
        "Systemic infections spread to internal organs, most commonly entering the body through this?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [132, 138, 147, 150, 161, 180, 184, 189, 190, 198, 200, 201, 208,
                222, 229, 236, 245, 247, 251, 253],
    _OVERLAP: [137, 187, 194, 215],
    _CONTEST: [151, 165, 168, 176, 178, 186, 219, 223, 254],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(130, 260)
    if f"validation-{n:05d}" not in EDITS
}
