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

mines = {
    '1 - mine de pierre' : choisisseurDeMine(1),
    '2 - mine de charbon' : choisisseurDeMine(2),
    '3 - mine de fer' : choisisseurDeMine(3)
}

def mineur(nombre, coups):
    while True:
        choix = input(nombre)
        coups = nombre * (5-mines[mineChoisie])
        return coups


for type in mines.keys():
    print(type)

print("Choisissez la mine où vous souhaitez vous rendre:")
prompt = "type de mines"
mineChoisie = verifChoix(prompt, mines, "choisissez le numéro de la mine")

