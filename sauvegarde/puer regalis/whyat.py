sante_mentale = 100
distance = 0

objets = {
    "appareil":{
        "grémoire",
        "sak",
        }}

lieux = {
    "plaine":{
        "distance": 1,
        "menace": 1
        },
    "devastation": {
        "distance": 5,
        "menace": 10
    },
    "termitière": {
        "distance": 5,
        "menace": 25
    },
    "cavernes": {
        "distance": 10,
        "menace": 5
    },
    "extrémités obscures": {
        "distance": 50,
        "menace": 100
    },
    "wan-0": {
        "distance": 0,
        "menace": 0
    }
}

print("Vous vous trouvez dans une grande plaine où son espace vide s'étend à perte de vue. Le sol que vous foulez est sec et comme parsemé de minuscules fissure à se surface." \
"pourtant, un chemin vous fait face et vous tenez un genre d'appareil sur lequel un genre d'écran est éteint." \
"vous pouvez marcher, examiner ou attendre")

choix = input("que faites vous?")

def marcher():
    distance += 10
    for cle, value in lieux.items():
        sante_mentale -= value

def examiner():
    for cle, value in objets.items():
        print("l'objet que vous tenez et qui ressemble à un " + cle + " est en fait un " + value + ".")
    
