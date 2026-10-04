"""Hand-authored SciQ train edits: train-08250 .. train-08349."""

REVIEWED = ("train-08250", "train-08349")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-08266": (GC, "What was a particular rock commonly used for in ancient civilizations?"),
    "train-08269": (EF, "What device is used to measure a certain quantity?"),
    "train-08270": (EF, "What element has given properties?"),
    "train-08290": (GC, "Sediments in specific lakes contain large amounts of what?"),
    "train-08291": (EF, "What tides occur during particular moon phases?"),
    "train-08294": (EF, "People with which skin type run a greater risk of a certain health problem?"),
    "train-08295": (GC, "What happens to temperature in a given atmospheric layer as the altitude increases?"),
    "train-08313": (EF, "Where does a specific stage of digestion occur?"),
    "train-08330": (GC, "How many daughter cells are created at the end of a particular cell division process?"),
    "train-08337": (EF, "Which instruments are used to measure a certain feature of a volcano?"),
    "train-08345": (GC, "Given common human diseases are caused by types of what?"),
    "train-08349": (EF, "What body part includes a specific bone?"),
}
