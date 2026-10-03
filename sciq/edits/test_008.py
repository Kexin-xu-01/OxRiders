"""Hand-authored SciQ adversarial edits: test-00690 .. test-00819."""

EDITS = {
    "test-00698": ("generalize_to_category",
        "In relation to electrical current, what property will one wire have more of than another?"),
    "test-00702": ("drop_qualifier",
        "In the body, in which organ does a stage of digestion take place?"),
    "test-00707": ("drop_qualifier",
        "What type of mirror is shaped like part of a bowl?"),
    # freezing at low, boiling at high
    "test-00708": ("generalize_to_category",
        "When do gases and liquids change state?"),
    "test-00711": ("generalize_to_category",
        "What are hair-like structures on cells called?"),
    "test-00720": ("generalize_to_category",
        "What term describes how a vertebrate's internal temperature is regulated?"),
    # field reversals: old rocks point north or south depending on age
    "test-00733": ("exchange_feature",
        "Where do ancient rocks point towards on earth?"),
    "test-00740": ("drop_qualifier",
        "During a human pregnancy, which trimester exhibits rapid change?"),
    # carpals/metacarpals -> hand, tarsals/metatarsals -> foot
    "test-00760": ("generalize_to_category",
        "Small articulated bones comprise what part of the body?"),
    "test-00764": ("generalize_to_category",
        "What type of climate does the coast of a country have?"),
    "test-00767": ("generalize_to_category",
        "An element is in what form of matter?"),
    "test-00785": ("generalize_to_category",
        "What is one of the outer planets of our solar system?"),
}

_ONLY = "only one option is plausible under any edit"
_NONSENSE = "distractors are nonsense"
_CONTEST = "original key is contestable"
_OVERLAP = "options overlap"
_flag = {
    _ONLY: [690, 692, 693, 695, 696, 697, 699, 700, 703, 706, 712, 715, 716, 717,
            719, 722, 723, 725, 727, 729, 731, 732, 734, 736, 738, 739, 741, 742,
            744, 745, 746, 747, 748, 749, 753, 755, 756, 757, 758, 759, 761, 762,
            766, 768, 769, 770, 772, 773, 775, 776, 777, 778, 779, 780, 782, 783,
            784, 786, 787, 789, 790, 791, 792, 793, 794, 795, 797, 798, 799, 802,
            803, 804, 805, 806, 807, 809, 810, 811, 814, 815, 816, 817, 818, 819],
    _NONSENSE: [694, 705, 709, 713, 721, 726, 728, 735, 752, 754, 763, 774, 781,
                800, 808, 812],
    _CONTEST: [704, 710, 714, 724, 730, 737, 743, 750, 751, 771, 796, 801, 813],
    _OVERLAP: [691, 701, 718, 765, 788],
}
FLAGGED = {f"test-{n:05d}": reason for reason, ns in _flag.items() for n in ns}
