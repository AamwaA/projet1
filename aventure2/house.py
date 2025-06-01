import math
import random


print("La maison : Ceux des Angles")

ma_maison = {"chambre": 0, "couloir": 1, "toilettes": 1, "salle de bain": 2, "bureau": 5, "escaliers": 1, "salon": 2, "cuisine": 3, "entrée": 2, "cave": 4}

menace = 0
while menace == 0:
    print("Vous êtes dans votre maison, un bruit infime mais très net vous laisse une sensation etrange. il y a quelqu'un chez...")
    print("voici une liste des pièces de votre maison")
    for cle,valeur in ma_maison.items():
        print(cle)
    choice = input("dans quelle pièce voulez-vous vous rendre? ")
    if choice == cle:
        menace += valeur
    if menace < 0:
        print("la menace s'est aggrandie, l'intensité de sa menace à augmenté de " + str(menace) + ".")