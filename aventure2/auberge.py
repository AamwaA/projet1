import random

chambres = 10

print("Vous êtes le patron d'une petite auberge, situé sur le chemin d'un donjon mineur")
print("Vous accueillez des aventurier en mal d'aventure qui passeront une à plusieurs nuits dans votre établissement")
print("votre auberge possède " + str(chambres) + " chambres et à de quoi nourrir des aventurier pendant toute une semaine")

aventurier = {
    "race": {
        "humain",
        "elfe",
        "nain",
        "gnome"
},
    "niveau": {
        1,
        5,
        7,
        9,
    },
    "nuités": {
        1,
        2,
        3,
    }}

def Genaventurier():
    race = random.choice[aventurier]["race"]
    niveau = random.choice[aventurier]["niveau"]
    nuites = random.choice(aventurier["nuités"])
    pnj = list(race, niveau, nuites)
    return pnj

Genaventurier()

print("Une passe derrière votre fenêtre,")
print("La porte s'ouvre dans un grincement strident")
print("C'est un aventurier en quête de gloire")
print("Il a besoin de se reposer pour" + str(nuites) + " nuités das votre auberge")
print("Aux trais de son visage et de sa carrure, vous reconnaisesz un " + str(race))
print("grâce à votre expérience d'aventurier, vous l'estimez de niveau " + str(niveaux))
    
    
