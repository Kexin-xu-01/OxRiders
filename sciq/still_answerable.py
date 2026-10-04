"""Self-answer filter: authored edits that are still answerable.

Each authored question_adversarial was answered blind from its option pool.
Where one option could still be picked with confidence, the edit failed and the
row is dropped from sciq-adversarial-authored.csv. It is kept in
sciq-adversarial.csv with needs_review=yes and review_class=still_answerable.

id -> the option that still wins, and why
"""

STILL_ANSWERABLE = {
    # validation
    "validation-00012": "prolactin: milk production is its defining role",
    "validation-00035": "eight: the noble-gas octet is the textbook answer",
    "validation-00041": "mitosis: standard answer for eukaryotic cell division",
    "validation-00068": "circles: textbook motion of water particles in a wave",
    "validation-00110": "chloroplasts: 'plants and algae' still signals photosynthesis",
    "validation-00164": "equator: the only full circle among the reference lines",
    "validation-00192": "species: intraspecific competition is the obvious reading",
    "validation-00497": "mercalli scale: 'intensity' still pins it",
    "validation-00875": "46: normal human somatic cells",
    "validation-00883": "aorta: 'principal' vessel leaving the heart",
    "validation-00954": "liquid: a body of water is liquid",
    "validation-00960": "radial symmetry: textbook echinoderm answer",
    # test
    "test-00031": "mechanical energy: total energy of a moving object",
    "test-00046": "central nervous system: every brain region belongs to it",
    "test-00069": "metamorphosis: the term for that transformation",
    "test-00072": "kidneys: blood filtration by specialized structures",
    "test-00082": "methane: main component of fuel gas",
    "test-00083": "kidneys: only option that regulates blood substances",
    "test-00098": "visible light: narrow band, small part of the spectrum",
    "test-00123": "ethylene: the only gas among the options tied to synthesis",
    "test-00125": "head: lateral flexion plus rotation",
    "test-00129": "muscles: the 'musculo' in musculoskeletal",
    "test-00166": "sulfonate: the standard other surfactant head group",
    "test-00170": "brain: the human/chimp size difference",
    "test-00184": "digestive system: secretes enzymes (endocrine secretes hormones)",
    "test-00201": "mitochondria: matrix is its interior",
    "test-00204": "lungs: each in its own pleural cavity",
    "test-00212": "protons and electrons: fixed for a pure element, neutrons vary",
    "test-00228": "carbon dioxide: product of burning organic matter",
    "test-00265": "friction: the only surface force among the options",
    "test-00272": "two meters: well-known DNA length per nucleus",
    "test-00302": "ore: the definition",
    "test-00336": "two: bonding and antibonding",
    "test-00424": "melting: the only ice phase change offered",
    "test-00445": "tundra: land defined by permafrost",
    "test-00457": "hydrogen: the C/H/O trio",
    "test-00471": "passenger pigeon: 'once common' rules out the dodo",
    "test-00498": "metamorphic: rock formed by changing existing rock",
    "test-00534": "topographic: map of landscape features",
    "test-00637": "it bends: refraction",
    "test-00711": "cilia: hair-like cell structures",
    "test-00825": "winter: its start has the shortest days",
    "test-00860": "carbon: basis of biological molecules",
    "test-00948": "slump: the description is still complete",
}
