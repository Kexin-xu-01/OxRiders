"""Hand-authored SciQ train edits: train-07150 .. train-07249."""

REVIEWED = ("train-07150", "train-07249")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-07156": (EF, "What is the molecule with a particular mass rank?"),
    "train-07162": (EF, "What are electrons at a certain energy level of an atom called?"),
    "train-07164": (EF, "The molecular formula is a given formula, which is the same formula as?"),
    "train-07180": (GC, "What do specific bone cells do to bone?"),
    "train-07200": (GC, "Particular habitats are examples of what type of biome?"),
    "train-07204": (EF, "What is the only class of animals that has a certain body covering?"),
    "train-07210": (GC, "How many years can carbon be stored in a given reservoir?"),
    "train-07214": (GC, "Are specific organisms a new or old species on the earth?"),
    "train-07215": (EF, "What kind of surface would cause a particular kind of reflection?"),
    "train-07221": (EF, "What's the most common disorder from a certain chromosome abnormality?"),
}
