"""Hand-authored SciQ train edits: train-06550 .. train-06649."""

REVIEWED = ("train-06550", "train-06649")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-06550": (EF, "What type of cells are the human cells with a particular size rank?"),
    "train-06559": (EF, "What type of pollutants enter the air in a certain way?"),
    "train-06565": (EF, "What part of the brain has a given location and function?"),
    "train-06567": (GC, "What is a primary source of a specific hormone?"),
    "train-06568": (GC, "How many more times likely are men to suffer from a particular condition?"),
    "train-06574": (EF, "A certain kind of cell death is also known as?"),
    "train-06575": (GC, "What happens to the mass number during a given nuclear decay process?"),
    "train-06598": (EF, "What is the type of organic compound with a specific distinction?"),
    "train-06602": (EF, "What type of cellular respiration occurs under particular oxygen conditions?"),
    "train-06609": (EF, "Which metal has a certain property at room temperature?"),
    "train-06610": (EF, "How do molecules react when a gas undergoes a given temperature change?"),
    "train-06616": (GC, "What are the most common causes of brain injuries in a specific group?"),
    "train-06622": (EF, "The type of vesicle transport that moves a substance in a particular direction is called?"),
    "train-06635": (GC, "What is the primary component of a certain alloy?"),
    "train-06644": (EF, "Light with a given wavelength appears as what color?"),
    "train-06646": (GC, "What is the term for atherosclerosis of arteries that supply a specific organ?"),
}
