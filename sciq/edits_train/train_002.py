"""Hand-authored SciQ train edits: train-00100 .. train-00249."""

REVIEWED = ("train-00100", "train-00249")

EDITS = {
    "train-00108": ("generalize_to_category",
        "How many different types of taste can be detected by the taste buds of a particular animal?"),
    "train-00111": ("generalize_to_category",
        "How many amino acids make up a certain peptide?"),
    # red->blue in base, blue->pink/red in acid
    "train-00125": ("drop_qualifier",
        "Litmus paper turns what color when placed in a certain solution?"),
    # celsius vs fahrenheit pairs are both offered
    "train-00138": ("drop_qualifier",
        "What are the boiling and freezing points of water on a given temperature scale?"),
    # stress -> sexual, favorable -> asexual
    "train-00147": ("exchange_feature",
        "What type of reproduction usually occurs during certain environmental conditions?"),
    "train-00153": ("generalize_to_category",
        "How many types of a specific kind of wave are there?"),
    # cation vs anion
    "train-00178": ("generalize_to_category",
        "Ions of a certain kind have what type of charge?"),
    # H+ (acids) vs OH- (bases)
    "train-00202": ("drop_qualifier",
        "What are the compounds that produce certain ions when dissolved in water?"),
    "train-00203": ("drop_antecedent",
        "The atomic number of tungsten is 74, so a neutral tungsten atom has 74 electrons. "
        "How many electrons are in a neutral atom of another element?"),
    "train-00213": ("drop_qualifier",
        "In a monogamous pairing, an individual is generally paired with what other type of individual?"),
    "train-00234": ("exchange_feature",
        "Which form of electromagnetic waves does a particular source emit: low frequency or high frequency waves?"),
}
