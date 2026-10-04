"""Hand-authored SciQ train edits: train-06650 .. train-06749."""

REVIEWED = ("train-06650", "train-06749")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-06672": (EF, "What is a particular element in organic compounds?"),
    "train-06680": (GC, "What is the color of a certain metal oxide?"),
    "train-06684": (EF, "What mineral helps combat a given condition?"),
    "train-06692": (GC, "What type of tissue is a specific tissue?"),
    "train-06697": (EF, "What type of power is generated using a particular kind of resource?"),
    "train-06708": (EF, "Energy of a certain kind in a person or object is called?"),
    "train-06713": (EF, "What is the name of blood vessels that carry blood in a given direction relative to the heart?"),
    "train-06730": (EF, "What travels at a specific rate?"),
    "train-06744": (EF, "As the population changes in a particular way, competition for food does what?"),
}
