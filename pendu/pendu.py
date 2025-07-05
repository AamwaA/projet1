import random
from names import names
from utilitaire import joueur

print("difficulté: facile(1), moyenne(2), difficile(3)")
choixdif = input("quelle difficulté?")
if choixdif == "1":
    mot = random.choice(names["facile"])
if choixdif == "2":
    mot = random.choice(names["moyenne"])
if choixdif == "3":
    mot = random.choice(names["difficile"])


print(mot)

print(f"vous avez choisit un mot de {len(mot)} lettres")

motjoueur = []

while str(motjoueur) is not len(mot):
    ltr = input("quelle lettre?")
    if ltr in mot:
        print(ltr)
        motjoueur.append(ltr)
        print(motjoueur)
    else:
        print("cette lettre n'est pas dans le mot")
        joueur.pvrestant()
        print(motjoueur)
        if joueur.pv == 0:
            print("vous n'avez pas trouvé le mot")
            print("vous êtes mort pendu")
            break
    
