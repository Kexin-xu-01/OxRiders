"""Hand-authored SciQ train edits: train-07950 .. train-08049."""

REVIEWED = ("train-07950", "train-08049")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-07965": (GC, "What is the ph level for a particular liquid?"),
    "train-07973": (EF, "What are the most common lipids in a certain biological structure?"),
    "train-07985": (EF, "In a neutral atom, the atomic number is the same as the number of what?"),
    "train-07988": (EF, "What is the name for substances with a given ph range?"),
    "train-08005": (GC, "Specific molecules in cellular reactions work to do what to the reaction?"),
    "train-08009": (GC, "The job of a particular cell structure is to build what?"),
    "train-08012": (EF, "What action is the single biggest use of water in a certain setting?"),
    "train-08026": (EF, "What is the algae group with a given size and complexity?"),
    "train-08028": (GC, "How long do specific isotopes require to decay to a safe level in a nuclear reactor?"),
    "train-08031": (EF, "Teeth in a particular part of the mouth are used for what?"),
    "train-08033": (EF, "Water is primarily present in what state in a certain location?"),
    "train-08034": (EF, "What kind of respiration allows production of atp in given oxygen conditions?"),
    "train-08046": (EF, "E. coli uses how many enzymes for a specific metabolic task?"),
}
