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
while force > 100:
    result = input(prompt)
    try:
        force = int(result)
    except:
        print("Un chiffre cohérent svp...")

'''dv_ennemi = {"gobelin": 1, "orc": 2, "troll": 3, "géant": 4}

print("Vous voulez maintenant combattre un ennemi")
dv_ennemi = str(input("c'est tout à votre honneur, vous pouvez choisir entre un gobelin, un orc, un troll ou un géant. lequel vous semble a votre mesure?"))
pv_ennemi = random.randrange(50, 100, 5) * int(dv_ennemi)
print("très bien ! vous allez donc vous battre contre un " + str(dv_ennemi) + " ,un ennemi à " + int(pv_ennemi) + " points de vie.") '''

pv_ennemi = 200

force_ennemi = 20

# faire une boucle pour baisser les points de vie
# faire une boucle pour utiliser des potions
# faire une condition de victoire et de défaite

coup = force_ennemi * 1 #dv_ennemi
dv_perdus = 0

while pv_ennemi > 0:
    print("Que voulez vous faire?")
    print(" 1 - attaquer")
    print(" 2 - bloquer")
    print(" 3 - fuir")
    choice = input("Saisissez votre choix")
    if choice == '1':
        pv_ennemi -= force
        dv_perdus += force
        print("il reste " + str(pv_ennemi) + " points de vie à l'ennemi")
        if dv_perdus >= 20:
            dv_perdus = 0
            pv -= coup
            print("l'ennemi attaque, il vous reste" + str(pv) + " points de vie")
    if pv <= 0:
        print("Vous êtes mort")
        break
    if pv_ennemi <= 0:
        print("vous avez vaincu votre ennemi")

pv_potion = random.randrange(10, 101, 10)
loot_ennemi = ("hache", "épée", "armure", "bourse")

while pv_ennemi <= 0:
    print("Que voulez vous faire?")
    print(" 1 - boire une potion")
    print(" 2 - fouiller votre enemi")
    print(" 3 - partir d'ici")
    choice = input("Saisissez votre choix")
    if choice == '1':
        pv += pv_potion
    if pv < 100:
        pv = 100
    print("vous avez récupéré " + str(pv_potion) + " points de vie. vous en avez désormais " + str(pv) + ".")
    if choice == '2':
        loot = random.choice(loot_ennemi)
        print("vous avez récupérer sur votre ennemi une " + str(loot) + ".")
    if choice == '3':
        pv_ennemi = 200
        print("vous décidez de quitter la pièce")


'''if int(dv_ennemi) < 0:
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
    #print("Vous avez triomphé !")'''



