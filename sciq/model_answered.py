"""Model-answer filter (stricter second pass over rows kept by still_answerable.py).

The authoring model answered every remaining question_adversarial with the 5
options shuffled, "I don't know" included, picking a substantive option whenever
one looked more likely than the rest. A row survives only if "I don't know" was
the pick. Rows listed here are dropped from sciq-adversarial-authored.csv and kept
in sciq-adversarial.csv with review_class=model_answered.

id -> option the model picked
"""

MODEL_ANSWERED = {
    "validation-00020": "chlamydia", "validation-00032": "increases",
    "validation-00065": "carbohydrates", "validation-00067": "landslides",
    "validation-00099": "hemoglobin", "validation-00160": "urinary system",
    "validation-00191": "sexually", "validation-00202": "webbed",
    "validation-00244": "respiratory system", "validation-00279": "catalytic converters",
    "validation-00288": "neutrophils", "validation-00329": "granite",
    "validation-00354": "earthquake", "validation-00402": "the blue whale",
    "validation-00417": "carbohydrates", "validation-00452": "kidney",
    "validation-00515": "constellations", "validation-00539": "hemophilia",
    "validation-00570": "negative feedback", "validation-00649": "gills",
    "validation-00727": "second law", "validation-00744": "calcium",
    "validation-00816": "high", "validation-00846": "trachea",
    "validation-00854": "loud sounds", "validation-00870": "smooth muscle",
    "validation-00874": "deciduous", "validation-00912": "carbon",
    "validation-00937": "fluorine", "validation-00962": "lightning",
    "test-00003": "elevation", "test-00004": "tree rings", "test-00007": "deciduous",
    "test-00016": "wings", "test-00018": "feldspar and quartz", "test-00019": "temperature",
    "test-00020": "diffusion", "test-00022": "bruising", "test-00025": "cardiovascular system",
    "test-00032": "retina", "test-00039": "dead organisms", "test-00042": "plaque",
    "test-00044": "voltages", "test-00047": "enzymes", "test-00048": "genetic drift",
    "test-00053": "food", "test-00058": "central nervous", "test-00059": "smooth",
    "test-00060": "pi bonds", "test-00061": "14th", "test-00062": "invertebrate",
    "test-00068": "motion", "test-00081": "teeth", "test-00086": "a marsupial",
    "test-00087": "parasitic", "test-00092": "torque", "test-00094": "vision",
    "test-00100": "pons", "test-00105": "kinetic", "test-00115": "cancer",
    "test-00124": "hair", "test-00130": "acids", "test-00153": "nitrogen",
    "test-00156": "mouse", "test-00161": "crust, mantle, core",
    "test-00164": "skeletal muscle fibers", "test-00182": "shark", "test-00187": "first",
    "test-00190": "osmosis", "test-00197": "pulmonary circulation", "test-00211": "chemical",
    "test-00217": "Jupiter", "test-00219": "carbohydrates", "test-00235": "second",
    "test-00237": "three", "test-00263": "cone-bearing plants", "test-00289": "binary fission",
    "test-00291": "exoskeleton", "test-00298": "along stream beds", "test-00305": "tumor",
    "test-00306": "pituitary", "test-00308": "porous", "test-00320": "pollinate",
    "test-00323": "respiratory", "test-00332": "lungs", "test-00343": "gas exchange",
    "test-00349": "oceanic crust", "test-00352": "meiosis", "test-00362": "autoimmune",
    "test-00379": "hemodialysis", "test-00383": "jupiter", "test-00401": "sublimation",
    "test-00418": "base", "test-00425": "homologous", "test-00430": "constellations",
    "test-00455": "hydrocarbons", "test-00483": "chewing", "test-00491": "their roots",
    "test-00496": "kinematics", "test-00512": "chemical", "test-00516": "nonmetals",
    "test-00520": "thyroid", "test-00535": "decreases", "test-00546": "commensalism",
    "test-00559": "slowly", "test-00566": "200", "test-00568": "covalent",
    "test-00576": "bacteria", "test-00582": "every 12 hours", "test-00583": "growth phase 2",
    "test-00587": "milk", "test-00607": "mothers", "test-00641": "hearing",
    "test-00644": "asteroids", "test-00698": "resistance", "test-00702": "small intestine",
    "test-00707": "concave", "test-00733": "north magnetic pole", "test-00740": "first trimester",
    "test-00785": "neptune", "test-00829": "at an angle", "test-00835": "bacteria",
    "test-00870": "sweat gland", "test-00885": "covalent", "test-00905": "hydrogen",
    "test-00918": "five", "test-00941": "progesterone", "test-00989": "secondary",
}
