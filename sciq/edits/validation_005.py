"""Hand-authored SciQ adversarial edits: validation-00520 .. validation-00649."""

EDITS = {
    "validation-00528": ("drop_list_member",
        "What planet has no oxygen and an atomsphere comprised mainly of carbon dioxide?"),
    "validation-00539": ("generalize_to_category",
        "What is a genetic disorder of the blood?"),
    "validation-00564": ("drop_superlative",
        "What decomposers can break down plant substances such as cellulose?"),
    "validation-00570": ("exchange_feature",
        "What form of feedback occurs when an accumulation of an end product changes the process that makes that product?"),
    # bromine is liquid
    "validation-00581": ("generalize_to_category",
        "What phase is a pure halogen present as?"),
    # cnidarians two, flatworms three
    "validation-00587": ("generalize_to_category",
        "How many embryonic cell layers do invertebrate animals have?"),
    "validation-00609": ("drop_qualifier",
        "What is the mode of breathing that occurs at a given activity level?"),
    "validation-00611": ("drop_qualifier",
        "What do birds of a particular species do in mating season?"),
    "validation-00620": ("exchange_feature",
        "If the number of coils in an electromagnet is changed, it becomes?"),
    "validation-00647": ("generalize_to_category",
        "What type of climate do most species of a plant genus grow in?"),
    # sponges filter through pores
    "validation-00649": ("generalize_to_category",
        "Invertebrates use what to filter food out of water?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_TRUNC = "question text truncated in source"
_reasons = {
    _NONSENSE: [520, 525, 530, 531, 537, 540, 541, 545, 558, 561, 565, 572, 575,
                577, 592, 596, 598, 606, 608, 612, 613, 615, 618, 621, 624, 639,
                640, 641, 643],
    _OVERLAP: [546, 563, 586],
    _CONTEST: [549, 557, 562, 579, 593, 601, 603],
    _TRUNC: [532, 550, 584],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"validation-{n:05d}": _special.get(n, _ONLY)
    for n in range(520, 650)
    if f"validation-{n:05d}" not in EDITS
}
