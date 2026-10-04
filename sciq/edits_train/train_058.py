"""Hand-authored SciQ train edits: train-05950 .. train-06049."""

REVIEWED = ("train-05950", "train-06049")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-05953": (EF, "Where in the body does production of a particular gamete take place?"),
    "train-05958": (GC, "In animals, how many sets of chromosomes do certain cells have?"),
    "train-05963": (GC, "Negative feedback controls secretion of a given hormone by what organ?"),
    "train-05975": (EF, "Which of newton's laws shows a specific relationship?"),
    "train-05993": (EF, "What do you need to do to water to change it to a particular state?"),
    "train-06001": (EF, "What planet in our solar system has a moon with a certain feature?"),
    "train-06002": (GC, "Given animals are examples of what type of mammals?"),
    "train-06014": (GC, "A specific disease is caused by injury to what organ as it is developing?"),
    "train-06015": (GC, "What substance is removed from waste as it passes through a particular organ?"),
    "train-06028": (GC, "At what time of life does a certain event occur?"),
    "train-06036": (EF, "Most amphibians breathe with these at a given life stage?"),
    "train-06041": (EF, "Does air temperature increase or decrease with height in a specific atmospheric layer?"),
}
