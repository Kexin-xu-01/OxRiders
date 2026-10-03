"""Hand-authored SciQ adversarial edits: test-00820 .. test-00999."""

EDITS = {
    "test-00824": ("generalize_to_category",
        "A primary cortex is located in which lobe of the brain?"),
    "test-00825": ("drop_superlative",
        "The beginning of what season experiences a short period of daylight hours?"),
    "test-00829": ("drop_quantifier",
        "Do waves strike the shore head on or at an angle?"),
    # amphibians absorb oxygen through skin; reptiles lose neither water nor gas
    "test-00832": ("generalize_to_category",
        "What are animals with scaly skin unable to absorb through their skin?"),
    "test-00835": ("generalize_to_category",
        "What organisms become parasitic and cause disease in humans?"),
    "test-00844": ("drop_list_member",
        "Besides photosynthesis, how can protists get their food?"),
    "test-00860": ("generalize_to_category",
        "What element is present in most molecules of living things?"),
    "test-00862": ("generalize_to_category",
        "An infectious disease causes inflammation of which organ?"),
    "test-00863": ("drop_qualifier",
        "If a substance has a ph value other than 7, what does it indicate?"),
    "test-00870": ("drop_qualifier",
        "What type of gland is found all over the body and secretes onto the skin?"),
    "test-00885": ("drop_qualifier",
        "What bond is the force of attraction that holds together two atoms?"),
    "test-00894": ("generalize_to_category",
        "What happens to water when it changes state?"),
    "test-00905": ("drop_superlative",
        "What element is abundant in the universe?"),
    # "big five" vs counts that include later or minor events
    "test-00918": ("drop_qualifier",
        "How many extinction events have occurred throughout earth's history?"),
    # estrogen also suppresses follicle development via negative feedback
    "test-00941": ("drop_list_member",
        "What ovarian hormone prevents new ovarian follicles from developing?"),
    "test-00948": ("drop_qualifier",
        "What leaves behind scars on a hillside and may be caused by a layer of slippery, wet clay underneath the rock and soil?"),
    "test-00951": ("generalize_to_category",
        "How many chambers are there in a vertebrate's heart?"),
    "test-00960": ("generalize_to_category",
        "Where do lymphocytes mature?"),
    "test-00970": ("merge_alternatives",
        "What is the term for something changing between water and ice?"),
    "test-00976": ("drop_qualifier",
        "Where do igneous rocks cool at?"),
    "test-00982": ("drop_qualifier",
        "What is a solution with a ph other than 7 called?"),
    "test-00989": ("drop_qualifier",
        "Carnivores are what kind of consumers?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_reasons = {
    _NONSENSE: [831, 837, 846, 848, 851, 866, 901, 920, 926, 934, 937, 950, 958,
                973, 978],
    _OVERLAP: [843, 868, 886, 889, 898, 980, 998],
    _CONTEST: [821, 872, 923, 927, 949, 954, 957, 993, 996, 999],
}
_special = {n: r for r, ns in _reasons.items() for n in ns}
FLAGGED = {
    f"test-{n:05d}": _special.get(n, _ONLY)
    for n in range(820, 1000)
    if f"test-{n:05d}" not in EDITS
}
