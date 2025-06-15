import math
import random


print("La maison : Ceux des Angles")

ma_maison = {"chambre": 0, "couloir": 1, "toilettes": 1, "salle de bain": 2, "bureau": 5, "escaliers": 1, "salon": 2, "cuisine": 3, "entrée": 2, "cave": 4}


menace = 0
for cle,valeur in ma_maison.items():
    while menace == 0:
        print("Vous êtes dans votre maison, un bruit infime mais très net vous laisse une sensation etrange. il y a quelqu'un chez...")
        print("voici une liste des pièces de votre maison")
        print(cle)
        choice = input("dans quelle pièce voulez-vous vous rendre? ")
        if choice == str(cle):
            ma_maison[cle] = valeur
            menace += valeur
        if menace >= 0:
            print("vous vous retrouvez dans : " + str(choice) + ". La menace s'est aggrandie, l'intensité de sa menace à augmenté de " + str(menace) + ".")
            break
    while menace >= 0:
        print("l'ambiance de la maison à changé...")
        choice = input("dans quelle pièce voulez-vous vous rendre?")
        if choice == str(cle):
            menace += valeur
        if menace >= 5:
            menace += valeur
            print("la menace s'est aggrandie, l'intensité de sa menace à augmenté de " + str(menace) + ".")
            break
