class Race:
    def __init__(self, nom, attributs):
        self.nom = nom
        self.attribus = attributs

racepossible = {
    "humain": {
        "force": 1,
        "dextérité": 1,
        "constitution": 1,
        "intelligence": 1,
        "sagesse": 1,
        "charisme: 1"
    },
    "elfe": {
        "force": 0,
        "dextérité": 2,
        "constitution": 0,
        "intelligence": 0,
        "sagesse": 2,
        "charisme: 2"
    },
    "nain": {
        "force": 2,
        "dextérité": 0,
        "constitution": 2,
        "intelligence": 2,
        "sagesse": 0,
        "charisme: 0"
    }
}