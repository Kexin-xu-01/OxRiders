"""Hand-authored SciQ train edits: train-06750 .. train-06849."""

REVIEWED = ("train-06750", "train-06849")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-06764": (GC, "What are clouds on a particular planet made of?"),
    "train-06769": (GC, "What unit is named for a certain scientist?"),
    "train-06775": (EF, "When is the sun directly over a given latitude?"),
    "train-06798": (GC, "When dissolved in water, a specific compound produces particular ions with what charge?"),
    "train-06806": (EF, "Alleles of a certain kind are represented by what case letter?"),
    "train-06812": (GC, "A given ice age took place in which era?"),
    "train-06819": (GC, "Do specific elements tend to gain electrons or lose electrons in chemical reactions?"),
    "train-06834": (EF, "What is the term for the structure that supports particular animals?"),
    "train-06835": (EF, "What gas moves through the airways during a certain phase of breathing?"),
    "train-06838": (EF, "What layer of skin is directly under a given layer?"),
    "train-06844": (EF, "What is a simple machine that consists of specific parts?"),
    "train-06848": (EF, "Which of the electromagnetic waves have particular wavelengths and frequencies?"),
}
