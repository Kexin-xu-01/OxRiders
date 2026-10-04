"""Hand-authored SciQ train edits: train-07850 .. train-07949."""

REVIEWED = ("train-07850", "train-07949")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-07853": (GC, "Where is a particular rock found?"),
    "train-07855": (GC, "Which type of diseases do certain drugs treat?"),
    "train-07861": (EF, "What term refers to an animal that is active at a given time of day?"),
    "train-07865": (EF, "What is the element with a specific abundance rank in the universe?"),
    "train-07867": (GC, "What disease is caused by a particular vitamin deficiency?"),
    "train-07895": (GC, "A certain prenatal stage begins about how long after fertilization?"),
    "train-07913": (EF, "What type of plant has a given leaf pattern through the year?"),
    "train-07920": (GC, "Specific organs are part of what body system?"),
    "train-07929": (EF, "If the experimental value differs from the accepted value in a particular direction, the error is what?"),
    "train-07932": (GC, "How many types of certain subatomic particles are there?"),
    "train-07941": (GC, "What kind of resource is a given natural material?"),
    "train-07944": (EF, "What hormone has a specific role in pregnancy and lactation?"),
    "train-07947": (EF, "What type of exercise has a particular intensity and duration?"),
}
