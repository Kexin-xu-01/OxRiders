"""Hand-authored SciQ train edits: train-10150 .. train-10249."""

REVIEWED = ("train-10150", "train-10249")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-10158": (GC, "One gram of a particular nutrient provides how many calories of energy?"),
    "train-10160": (GC, "How are certain protozoa spread?"),
    "train-10166": (GC, "A given material is an important part of the process used to harness which type of power?"),
    "train-10172": (GC, "How many layers does a specific biological structure contain?"),
    "train-10183": (EF, "Where do particular steps of cellular respiration take place?"),
    "train-10184": (EF, "Which metal has a certain state at room temperature?"),
    "train-10197": (EF, "What type of light has given wavelengths?"),
    "train-10206": (EF, "Ocean currents transfer heat from a specific region towards what locations?"),
    "train-10216": (GC, "A particular interaction between individuals of two different species has what effect on them?"),
    "train-10228": (GC, "During what period on earth was a certain resource formed?"),
    "train-10230": (EF, "Which vertebrates were the first with a given trait?"),
    "train-10234": (GC, "What is a specific age-related disorder of the skeleton?"),
    "train-10236": (EF, "Which bones form a particular part of the body?"),
    "train-10239": (EF, "What type of fertilization usually occurs in certain environments?"),
    "train-10247": (EF, "If everything else stays the same in a system with a gas in it, and the gas changes temperature in a given way, what will happen to its pressure?"),
}
