"""Hand-authored SciQ train edits: train-08850 .. train-08949."""

REVIEWED = ("train-08850", "train-08949")

EF, GC = "exchange_feature", "generalize_to_category"

EDITS = {
    "train-08853": (GC, "Are the majority of particular microbes chemotrophs or photosynthetic?"),
    "train-08858": (EF, "What are certain reproductive cells called?"),
    "train-08871": (EF, "What are plastids that contain given pigments?"),
    "train-08882": (EF, "A major diversification of what animal group occurred at a specific time?"),
    "train-08890": (EF, "What is another term for joints with a particular mobility?"),
    "train-08903": (EF, "The solution with a certain relative solute concentration is called what?"),
    "train-08907": (GC, "What do a given group of biological units working together form?"),
    "train-08912": (EF, "When sperm is deposited in a specific way during mating, this is considered what type of fertilization?"),
    "train-08913": (GC, "What part of the body does a particular bacterium usually attack?"),
    "train-08916": (EF, "In celsius, what is the temperature at which water undergoes a certain phase change?"),
    "train-08920": (GC, "Given consumers usually eat what?"),
    "train-08930": (EF, "What is defined as a specific change in hydrogen atoms?"),
    "train-08949": (GC, "A particular planet is covered with what objects?"),
}
