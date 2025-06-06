sante_mentale = 100
distance = 0

objets = {"appareil": "grémoire"}

lieux = {"plaine": 1}

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
    
