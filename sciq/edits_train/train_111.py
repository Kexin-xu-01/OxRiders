"""Hand-authored SciQ train edits: train-11250 .. train-11349."""

REVIEWED = ("train-11250", "train-11349")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-11250": (EF, "What is a person who studies a particular subject called?"),
    "train-11253": (GC, "What protects certain animals from drying out?"),
    "train-11255": (GC, "What gives a given cheese its color?"),
    "train-11259": (GC, "Where did a specific virus first appear?"),
    "train-11263": (GC, "About how many grams of carbohydrates are in a typical serving of a particular food?"),
    "train-11271": (EF, "An rna codon with a certain sequence encodes for what?"),
    "train-11272": (GC, "Given microscopes use what kind of waves to scan a specimen?"),
    "train-11274": (GC, "How many chambers are in a specific animal's heart?"),
    "train-11275": (EF, "What is a particular part in the front of the eye called?"),
    "train-11276": (EF, "When salinity, pressure, or temperature change in a certain way, what happens to water density?"),
    "train-11279": (GC, "What happens to structural genes in the presence of a given molecule?"),
    "train-11287": (GC, "A specific chemical reaction is what type of reaction?"),
    "train-11296": (EF, "A particular atomic radius is defined using which type of bond?"),
    "train-11301": (GC, "A certain geological event occurred in which period?"),
    "train-11312": (GC, "A given beetle bores holes in?"),
    "train-11317": (GC, "What country put a specific series of space stations into orbit?"),
    "train-11328": (GC, "Silicon and germanium react with a particular element at high temperature to form what?"),
    "train-11331": (EF, "The cell moves particles in a certain direction across its membrane through a process called what?"),
    "train-11335": (EF, "What term is used to describe a region getting a given amount of precipitation relative to normal?"),
    "train-11337": (GC, "What human disease is caused by a specific defective enzyme?"),
    "train-11349": (EF, "What do you call plastids that contain a particular pigment?"),
}
