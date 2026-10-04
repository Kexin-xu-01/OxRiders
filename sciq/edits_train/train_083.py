"""Hand-authored SciQ train edits: train-08450 .. train-08549."""

REVIEWED = ("train-08450", "train-08549")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-08456": (GC, "In a tropical rainforest, where are particular plants common?"),
    "train-08459": (GC, "A certain gene encodes which receptor?"),
    "train-08468": (GC, "How does the atomic number change during a given type of radioactive decay?"),
    "train-08471": (GC, "Where does a specific atmospheric layer get most of its heat?"),
    "train-08473": (GC, "What is the name of a particular moon in the solar system?"),
    "train-08481": (GC, "Certain mammals are part of what group?"),
    "train-08491": (EF, "What is the organ with a given superlative feature in the human body?"),
    "train-08499": (GC, "Name the type of system that specific animals do not have?"),
    "train-08500": (EF, "Organisms with a particular lifestyle store energy in what form?"),
    "train-08534": (EF, "What is the disease in which a certain part of the respiratory system is affected?"),
    "train-08538": (GC, "What bodily function does a given muscle help perform?"),
    "train-08549": (EF, "What is a form of matter that has specific volume and shape properties?"),
}
