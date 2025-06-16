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
mineurs = int(prompt)
coupDePioche = 3 * mineurs

print("vous avez donc avec vous " + str(mineurs) + " mineurs (des nains sans doute)")
print("Ils donneront chacun " + str(coupDePioche) + "coup de pioches (mais des coups efficaces)")

def heHo(prompt):
    mineursengagés = prompt
    chariot = []
    for i in range(mineursengagés):
        chariot.append(random.choices(list(mines[mineChoisie]))) * coupDePioche
    return chariot


prompt = input("combien de mineurs envoyez vous au travail aujourd'hui?")
heHo(int(prompt))

print(chariot)



