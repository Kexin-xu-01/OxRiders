"""Hand-authored SciQ train edits: train-08150 .. train-08249."""

REVIEWED = ("train-08150", "train-08249")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-08151": (EF, "What is the process in which a particular phase change occurs?"),
    "train-08153": (EF, "What is the planet with a certain size rank in the solar system?"),
    "train-08154": (EF, "What are elements required in given amounts?"),
    "train-08155": (EF, "What can be calculated from an object's mass in kilograms (kg) and a specific quantity?"),
    "train-08160": (EF, "What occurs when there is a particular amount of rain in a period of time?"),
    "train-08166": (GC, "Certain animals are which type of animal?"),
    "train-08167": (GC, "A given disease occurs most often in adults over what age?"),
    "train-08172": (EF, "What do you call the temperature at which a specific phase change occurs?"),
    "train-08178": (EF, "Light with particular wavelengths is called what?"),
    "train-08191": (GC, "Each atom of a certain element shares how many valence electrons with other atoms in a crystal?"),
    "train-08199": (EF, "A very small blood vessel of a given type is known as what?"),
    "train-08208": (EF, "Because specific particles have unequal numbers of protons and electrons, what kind of electric charge do they have?"),
    "train-08227": (GC, "Particular heterotrophs eat only or mainly what?"),
    "train-08236": (EF, "What is the name for a certain gamete?"),
}
