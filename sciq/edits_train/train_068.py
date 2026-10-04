"""Hand-authored SciQ train edits: train-06950 .. train-07049."""

REVIEWED = ("train-06950", "train-07049")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-06957": (EF, "What does a particular additive do to a certain phase-change temperature of the water in car radiators?"),
    "train-06959": (EF, "A given layer of the sun is known as what?"),
    "train-06966": (EF, "What is the organ that senses a specific stimulus?"),
    "train-06989": (EF, "What is a particular layer of skin called?"),
    "train-06991": (GC, "What does a certain instrument measure?"),
    "train-06994": (EF, "Given atoms in radioactive decay are called what type of isotopes?"),
    "train-06996": (GC, "In which continent are specific animals most likely to be found?"),
    "train-07003": (EF, "A particular count of particles in an atom is called what?"),
    "train-07018": (EF, "In glycolysis, glucose is split into two molecules of pyruvate. this results in a certain kind of gain of?"),
    "train-07041": (GC, "Given things move, but they aren't destroyed. this is the law of conservation of what?"),
}
