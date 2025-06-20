'''print("cour3")

niveau = 10
race = "orc"

if niveau > 5:
    if race == "orc":
        print("un orc expérimenté !")
    else:
        print("un vétéran non-orc")
else:
    print("un jeune aventurier")

for i in range(2):
    print("tour", i)

objets = ["épée", "bouclier", "potion"]

for i, objet in enumerate(objets):
    print(f"{i+1}. {objet}")

noms = ["orc", "orc", "elfe"]
noms_uniques = set(noms)
print(noms_uniques)

try:
    age = int(input("votre age?"))
except ValueError:
    print("ce n'est pas un nombre")'''


print("exercice 0")

nom = "Elyra"
objet = "hache"
degats = 100
rarete = "légendaire"

print(f"{nom} possède une {objet} ({rarete}) qui inflige {degats} points de dégats")

print("exercice 1")

joueur = {
    "nom": "Aelwyn",
    "or": 100,
    "inventaire": ["épée", "bouclier"]
}

magasin = {
    "lame de feu": 50,
    "cape d’invisibilité": 80,
    "potion de soin": 30
}

def afficherInventaire(joueur):
    print("inventaire joueur")
    for i, objet in enumerate(joueur["inventaire"]):
        print(f"{i+1}. {objet}")

def afficherMagasin(marchand):
    print("etal du magasin:")
    for i, objet in enumerate(marchand):
        print(f"{i+1}. {objet} - {marchand[objet]} pièces d'or")


def acheterObjet(joueur, objet, magasin):
    if objet in magasin:
        joueur["inventaire"].append(objet)
    else:
        print("Cet objet n'existe pas dans le magasin.")
    if joueur["or"] >= magasin[objet]:
        joueur["or"] -= magasin[objet]
        joueur["inventaire"].append(objet)
    else:
        print("Vous n'avez pas assez d'or !")
    joueur["or"] -= magasin[objet]


while joueur["or"] > 0:
    print("Vous vous trouvez dans un magasin")
    afficherMagasin(magasin)
    choix = input("que voulez-vous acheter?")
    acheterObjet(joueur, choix, magasin)
    print(f"vous avez acheter une {choix}, il vous reste {joueur['or']}")
    afficherInventaire(joueur)
    if joueur["or"] <= 0:
        print("vous n'avez plus d'argent")
        break

# notes d'exercice:
# 1: j'ai corriger mon code, mais celles-ci sont peut-être placées au mauvais endroit


print("exercice 2")

