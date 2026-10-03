"""Hand-authored SciQ adversarial edits: validation-00000 .. validation-00129."""

EDITS = {
    "validation-00012": ("exchange_feature",
        "What hormone regulates milk production in mammals?"),
    "validation-00020": ("drop_superlative",
        "What is a common sti?"),
    "validation-00032": ("drop_qualifier",
        "During a change in activity, the rate of blood returning to the heart does this?"),
    # helium has two, the rest eight
    "validation-00035": ("drop_quantifier",
        "How many valence electrons does a noble gas element have?"),
    "validation-00037": ("drop_qualifier",
        "What category of catalyst is used in a particular reaction?"),
    "validation-00041": ("drop_qualifier",
        "What is the process by which a eukaryotic cell divides?"),
    "validation-00043": ("exchange_feature",
        "What type of organism has its growth affected by the presence of oxygen?"),
    "validation-00065": ("drop_superlative",
        "What is a source of energy for your body?"),
    "validation-00067": ("drop_qualifier",
        "Earthquakes can also trigger what?"),
    # circles in deep water, ellipses in shallow water
    "validation-00068": ("drop_qualifier",
        "In which way do particles of water move in a wave?"),
    "validation-00071": ("drop_qualifier",
        "If you examine eyeglasses, what shape will you find the lenses are?"),
    "validation-00079": ("exchange_feature",
        "Research classified by whether it is concerned with usefulness is known as what kind of research?"),
    "validation-00086": ("drop_quantifier",
        "Is a particular glacier currently growing or shrinking?"),
    # beta-minus vs beta-plus
    "validation-00090": ("generalize_to_category",
        "Radioactive decay occurs when a nucleus has too few of what?"),
    "validation-00099": ("generalize_to_category",
        "What oxygen-binding pigment do certain cells contain?"),
    "validation-00104": ("drop_qualifier",
        "Is the yolk more or less concentrated toward this pole of the egg?"),
    "validation-00110": ("generalize_to_category",
        "What are the organelles where energy conversion takes place in plants and algae?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [6, 27, 30, 47, 53, 61, 64, 73, 84, 88, 93, 98, 118, 122, 126],
    _OVERLAP: [18, 49, 92, 121],
    _CONTEST: [2, 9, 14, 16, 22, 29, 76, 97, 107, 114],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(0, 130)
    if f"validation-{n:05d}" not in EDITS
}
