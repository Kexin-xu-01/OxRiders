"""Hand-authored SciQ train edits: train-07350 .. train-07449."""

REVIEWED = ("train-07350", "train-07449")

EF, GC, DQ = "exchange_feature", "generalize_to_category", "drop_qualifier"

EDITS = {
    "train-07351": (EF, "What would cause particular temperature receptors to signal the hypothalamic thermostat?"),
    "train-07374": (EF, "Making a statement by reasoning in a certain logical direction is the definition of what type of reasoning?"),
    "train-07382": (EF, "Which layer of soil experiences a given amount of weathering?"),
    "train-07392": (EF, "For a given amount of solute, do particles of a specific size have a greater or lesser surface area?"),
    "train-07401": (DQ, "Chromatin condenses into chromosomes during prophase of what process?"),
    "train-07423": (GC, "What is a particular heart symptom known as?"),
    "train-07427": (GC, "What is a certain weather phenomenon of whirling high winds known as?"),
    "train-07432": (EF, "How long does it take for the earth to make a given complete motion?"),
    "train-07435": (GC, "What form does water take on a specific planet?"),
    "train-07444": (EF, "What are particular antibodies an animal produces called?"),
    "train-07448": (GC, "A certain medical device uses electrical stimulation to make what work properly?"),
}
