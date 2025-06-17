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
        2,
        3,
        4,
    },
    "nuités": {
        1,
        2,
        3,
    }}

def genPnj(nombre, dicAv):
    locataires = liste(dicAv.keys())
    
