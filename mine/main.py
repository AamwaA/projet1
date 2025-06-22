import random

def verifChoix(prompt, liste, errorMessage="réessayez"):
    while True:
        choix = input(prompt)
        if choix in liste:
            return choix
        else:
            print(errorMessage)

def choisisseurDeMine(rateMine):
    ore = {
        "pierre": {
            "type": rateMine,
            "rareté": 1*rateMine,
            "prix": 5*rateMine,
        },
        "charbon": {
            "type": rateMine,
            "rareté": 2*rateMine,
            "prix": 10*rateMine,
        },
        "cristal": {
            "type": rateMine,
            "rareté": 5*rateMine,
            "prix": 15*rateMine
        },
        "fer": {
            "type": rateMine,
            "rareté": 10*rateMine,
            "prix": 25*rateMine,
        },
        "bronze": {
            "type": rateMine,
            "rareté": 25*rateMine,
            "prix": 40*rateMine,
        },
        "argent": {
            "type": rateMine,
            "rareté": 50*rateMine,
            "prix": 100*rateMine,
        },
        "or": {
            "type": rateMine,
            "rareté": 100*rateMine,
            "prix": 250*rateMine,
        }
}
    return ore

mineurs = 0



mines = {
    '1' : choisisseurDeMine(1),
    '2' : choisisseurDeMine(2),
    '3' : choisisseurDeMine(3)
}

chariot = []

print("Choisissez la mine où vous souhaitez vous rendre:")
print("1 - mine de pierre")
print("2 - mine de charbon")
print("3 - mine de fer")
prompt = "type de mines? "
mineChoisie = verifChoix(prompt, mines, "choisissez le numéro de la mine")

print(mines[mineChoisie])

prompt = input("combien de mineurs voulez-vous engager?")
équipe = int(prompt)


print("vous avez donc avec vous " + str(équipe) + " mineurs (des nains sans doute)")

def heHo(mineurs, dicMine):
    coupDePioche = 3 * mineurs
    minerais = list(dicMine.keys())
    poids = [1 / dicMine[ore]['rareté'] for ore in minerais]
    total = sum(poids)
    rarepicks = [p / total for p in poids]
    chariot = random.choices(minerais, weights=rarepicks, k=coupDePioche)
    return chariot

chariot = heHo(équipe, mines[mineChoisie])
print("Voici le contenu du chariot extrait :")
print(chariot)
