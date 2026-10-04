"""Hand-authored SciQ train edits: train-05850 .. train-05949."""

REVIEWED = ("train-05850", "train-05949")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-05850": (EF, "What process occurs around a particular day of a 28-day menstrual cycle?"),
    "train-05858": (EF, "What stage in human males lasts a certain range of years?"),
    "train-05867": (GC, "What happens to a given part of a star when it begins to run low on hydrogen?"),
    "train-05876": (GC, "What is the only metalloid in a specific group?"),
    "train-05878": (GC, "What type of minerals form when a particular solution evaporates?"),
    "train-05883": (GC, "A certain order is the largest order of what broad animal group?"),
    "train-05889": (EF, "What happens between particles with given charges?"),
    "train-05893": (EF, "What organs produce specific gametes?"),
    "train-05895": (GC, "How much larger can a particular microscope make an image?"),
    "train-05901": (GC, "What is the layer above a certain atmospheric layer?"),
    "train-05906": (GC, "What type of resource is a given energy source?"),
    "train-05926": (EF, "What is the name for a heterotroph with a specific diet?"),
    "train-05937": (GC, "What shape are the faces of a particular polyhedron?"),
}
