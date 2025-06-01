import math
import random


print("La maison : Ceux des Angles")
menace = 0

ma_maison = {"chambre": 0, "couloir": 1, "toilettes": 1, "salle de bain": 2, "bureau": 5, "escaliers": 1, "salon": 2, "cuisine": 3, "entrée": 2, "cave": 4}
for cle, valeur in ma_maison.items():
    while menace == 0:
        print("Vous êtes dans votre maison, un bruit infime mais très net vous laisse une sensation etrange. il y a quelqu'un chez...")
        print("voici une liste des pièces de votre maison")
        for cle in ma_maison.items():
            print(cle)
        choice = input("dans quelle pièce voulez-vous vous rendre? ")
        for valeur in ma_maison.values():
            if choice == cle:
                menace += valeur
        if menace <= 0:
            print("vous vous retrouvez dans : " + str(choice) + " la menace s'est aggrandie, l'intensité de sa menace à augmenté de " + str(menace) + ".")
            break
    while menace <= 0:
        print("l'ambiance de la maison à changé...")
        
        if menace <= 7:
            menace += valeur
            print("la menace s'est aggrandie, l'intensité de sa menace à augmenté de " + str(menace) + ".")
            break
