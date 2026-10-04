"""Hand-authored SciQ train edits: train-00000 .. train-00099.

REVIEWED  inclusive id range read in this batch; rows in it without an EDIT are flagged
EDITS     id -> (mechanism, unanswerable question)
"""

REVIEWED = ("train-00000", "train-00099")

EDITS = {
    # direction removed: exothermic vs endothermic
    "train-00002": ("drop_qualifier",
        "Changes between a less-ordered state and a more-ordered state are always what?"),
    # meteor (in the atmosphere) vs meteorite (on the ground)
    "train-00005": ("drop_qualifier",
        "What is a meteoroid called at a certain stage of its approach to earth?"),
    # induced vs spontaneous ending
    "train-00021": ("exchange_feature",
        "What is it called when a pregnancy ends in a particular way?"),
    # sex unstated: testosterone vs estrogen
    "train-00029": ("drop_qualifier",
        "What hormone helps bring about physical changes in puberty?"),
    "train-00047": ("exchange_feature",
        "How many people die from air pollution each year in a certain region?"),
    "train-00076": ("generalize_to_category",
        "How many chambers does the stomach of a given animal have?"),
    "train-00092": ("drop_quantifier",
        "What percentage of men suffer from some form of erectile dysfunction by a certain age?"),
}
