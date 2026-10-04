"""Hand-authored SciQ adversarial edits: test-00000 .. test-00039.

EDITS   id -> (mechanism, unanswerable question)
FLAGGED id -> reason no sound edit exists
"""

EDITS = {
    # accept vs donate is the whole distinction; antioxidants (reductants) now fit too
    "test-00000": ("drop_qualifier",
        "Compounds that are capable of transferring electrons are called what?"),
    # clone, adult and male all describe an individual organism
    "test-00001": ("generalize_to_category",
        "What term in biology describes an individual organism?"),
    # the phylum is unnamed
    "test-00002": ("generalize_to_category",
        "Members of a phylum are characterized by the presence of what?"),
    # above -> elevation, below -> depth; the direction is gone
    "test-00003": ("drop_qualifier",
        "What is the vertical distance from sea level called?"),
    # without varves, tree rings and fossils both qualify
    "test-00004": ("drop_list_member",
        "Ice cores and what else indicate the environmental conditions at the time of their creation?"),
    # organism removed: plant vs human hormones
    "test-00005": ("generalize_to_category",
        "What chemical signals control different processes?"),
    # the sex is unstated: egg only vs sperm only
    "test-00006": ("generalize_to_category",
        "Meiosis is part of gametogenesis in one of the two sexes, which is the production of what?"),
    # "tree" pinned the answer; plant type is open across deciduous, vines, shrubs
    "test-00007": ("generalize_to_category",
        "Which type of plant is dominant in temperate regions?"),
    # viscosity depends on chain length, which is removed
    "test-00008": ("drop_qualifier",
        "What kind of viscosity is found in hydrocarbons?"),
    # ridges range from ripples (inches) to mid-ocean ridges (km)
    "test-00010": ("generalize_to_category",
        "About how tall can geological ridges be?"),
    # on a reef, corals or crustaceans; "invertebrate" alone pinned insects
    "test-00011": ("generalize_to_category",
        "What are by far the most common invertebrates on a reef?"),
    # gonads and ducts exist in both sexes
    "test-00013": ("generalize_to_category",
        "Gonads and their ducts are organs in what system?"),
    # incandescent, LED and neon lamps work differently
    "test-00015": ("generalize_to_category",
        "How does an electric lamp produce visible light?"),
    # the arboreal habitat selected wings; with no habitat any feature fits
    "test-00016": ("drop_qualifier",
        "A bird ancestor developed what feature commonly associated with birds?"),
    # every option is a pair of common silicates once "two most" is gone
    "test-00018": ("drop_superlative",
        "What are two common silicates?"),
    # humidity, temperature and pressure are all measurable properties of air
    "test-00019": ("generalize_to_category",
        "What term describes a measurable property of the air?"),
    # water -> osmosis, solutes -> diffusion
    "test-00020": ("generalize_to_category",
        "Molecules move by what method across a membrane?"),
    # nucleus + membrane-bound organelles mark all eukaryotes: plant and animal
    "test-00021": ("exchange_feature",
        "Presence of a nucleus and membrane-bound organelles distinguishes what type of cell?"),
    # damaged skin vessels -> bleeding or bruising
    "test-00022": ("exchange_feature",
        "What happens when blood vessels in the skin of mammals are damaged?"),
    # condition generalized: fractures, epilepsy, senility all possible
    "test-00023": ("generalize_to_category",
        "What are people with a chronic illness at increased risk of?"),
    # chemical -> between atoms, nuclear -> inside atoms
    "test-00024": ("generalize_to_category",
        "Where is potential energy stored in matter?"),
    # the diseases are no longer characterized; several systems fit
    "test-00025": ("drop_qualifier",
        "By the year 2050, 25 percent of the population of the united states will be 60 years of age or older. the cdc estimates that 80 percent of those 60 years and older have one or more chronic diseases. which body system are they linked to?"),
    # "ammonium" pinned nitrogen; potassium and calcium also return as ions
    "test-00026": ("drop_qualifier",
        "Upon death of an organism, during decomposition, what returns to the soil in ionic form?"),
    # some insects (aphids) are asexual, others sexual
    "test-00027": ("drop_quantifier",
        "Some insects reproduce quickly and through what type of reproduction?"),
    # haplodiploidy removed; the adaptation is unnamed
    "test-00029": ("generalize_to_category",
        "Many species of rotifers exhibit an adaptation, which is a method of what?"),
    # ore unspecified: bauxite -> aluminum, chalcopyrite -> copper
    "test-00030": ("generalize_to_category",
        "What is the most abundant metal in the ore sample?"),
    # macroscopic object -> mechanical, particles -> thermal
    "test-00031": ("generalize_to_category",
        "What is the term for the total energy of a moving object?"),
    # pupil, iris and retina all interact with incoming light
    "test-00032": ("generalize_to_category",
        "What part of the eye interacts with incoming light?"),
    # vestibular and vascular systems both enter the brain stem
    "test-00034": ("drop_trailing_condition",
        "What system enters the brain stem?"),
    # vertebrates and triploblastic animals both have one
    "test-00035": ("drop_qualifier",
        "In what type of animals is a body cavity present?"),
    # two quantities, two different units
    "test-00036": ("merge_alternatives",
        "Electric currents and heat flow are measured in what?"),
    # garden plants include annuals, biennials and perennials
    "test-00037": ("generalize_to_category",
        "Garden plants are examples of what type of plant?"),
    # digestion and photosynthesis both feed metabolism
    "test-00038": ("drop_qualifier",
        "The products of what process are needed for cellular metabolism?"),
    # saprophytic -> dead, parasitic -> living
    "test-00039": ("drop_quantifier",
        "Fungi get organic compounds from what?"),
}

FLAGGED = {
    "test-00009": "options are near-synonyms (regular/normal) or nonsense; no edit leaves a principled tie",
    "test-00012": "sediments is the only physically possible option whatever is removed",
    "test-00014": "photosynthesis stays the only loss that turns plants into consumers",
    "test-00017": "original key is contestable (enzymes is also correct)",
    "test-00028": "stomach is the only acidic organ among the options under any edit",
    "test-00033": "fight-or-flight is the only real stress response among the options",
}
