import random
import math

print("Bonjour aventurier")
nom = input("Quel est votre nom champion?")

print("Enchanté " + nom + "! " + " Très joli nom.")

pv = 100
potion = random.randrange(2, 6, 1)

print("Vous avez " + str(pv) + " Points de vie, c'est déjà bien et comme je suis sympa je vais vous donner " + str(potion) + " potions de soin.")

print("Comme j'ai pas trop eût le temps de préparer ça, combien tu veux en Force?")
force = 0

# Il y a surement un problème dans la boucle, j'aimerais qu'elle vérifie les deux try en même temps, pour que ça change selon ce qu'on met

prompt = "Force?"
while force == 0:
    result = input(prompt)
    try: 
        force = int(result)
    except:
       print("Veuillez entrer un chiffre")
while force > 50:
    result = input(prompt)
    try:
        force = int(result)
    except:
        print("Un chiffre cohérent svp...")

print("Vous voulez maintenant combattre un ennemi")
dv_ennemi = input("c'est tout à votre honneur, mais sur une échelle de 1 à 4 comment estimez une menace a votre mesure!")
dv_ennemi = random.randrange(50, 100, 5) * int(dv_ennemi)
print("très bien ! vous allez donc vous battre contre un ennemi à " + str(dv_ennemi) + " points de vie.") 

force_ennemi = 50

# faire une boucle pour baisser les points de vie
# faire une boucle pour utiliser des potions
# faire une condition de victoire et de défaite

coup = int(force_ennemi) + int(dv_ennemi)

pv_restant = int(dv_ennemi) - int(force)


print("Que voulez vous faire?")
print(" 1 - attaquer")
print(" 2 - bloquer")
print(" 3 - fuir")
choice = input("Saisissez votre choix")
if choice == '1':
    pv_restant = int(dv_ennemi) - int(force)
    print("il reste " + str(pv_restant) + " points de vie à l'ennemi")
while pv_restant > 0:
    pv_restant = pv_restant - force
    print("il reste " + str(pv_restant) + " pv restant à l'annemi.")
    for pv_restant in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        pv = pv - coup
    print("il vous reste " + str(pv) + " points de vie")
    if pv <= 0:
        break
    print("Vous êtes mort")
if pv_restant <= 0:
    print("vous avez vaincu votre ennemi")


'''print("Que voulez vous faire?")
print(" 1 - boire une potion")
print(" 2 - fouiller votre enemi")
print(" 3 - partir d'ici")
choice = input("Saisissez votre choix")
if choice == '1':



if int(dv_ennemi) < 0:
    pv_restant = int(dv_ennemi) - int(force)
elif pv_restant < 0:
    pv = int(pv) - int(coup)
else:
    print("...")



prompt = "attaquer?"
while pv_restant < 0:
    result = input(prompt)
    try:
        int(pv_restant) == int(dv_ennemi)
    except:
        print("Vous avez triomphé !")


#if pv_ennemi == 0:
    #print("Vous avez triomphé !")
'''
