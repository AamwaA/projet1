import random
import math

print("Bonjour aventurier")
nom = input("Quel est votre nom champion?")

print("Enchanté " + nom + "! " + " Très joli nom.")

race = {"humain": 5, "nain": 7, "elfe": 3}

exp = 10
niveau = math.floor(exp/10)

for dv in race.values():
    pvj = dv*50*niveau
    forcej = (10-dv)*niveau

print("il y a trois race dans notre monde")
print("vous avez le choix de jouer :")
for choix in race.keys():
    print(choix)
print("les nains ont plus de point de vie, mais les elfes infligent plus de dégats")
print("les humains quand à eux, sont un bon entre deux")

prompt = "Race?"
for choix, dv in race.items():
    result = input(prompt)
    if result == str(choix):
        pvj = dv * 50
        forcej = (10 - dv) * 10
print("en tant que " + result + ", vous avez " + str(pvj) + " points de vie et " + str(forcej) + " en force.")
print("vous êtes de niveau " + str(niveau))


potion = random.randrange(2, 6, 1)
pv_potion = 50

print("C'est déjà bien et comme je suis sympa je vais vous donner " + str(potion) + " potions de soin.")

monstres = {"gobelin": 1, "orc": 2, "troll": 3, "géant": 4}

pv_ennemi = 0
force_ennemi = 0


print("Vous voulez maintenant combattre un ennemi")
print("c'est tout à votre honneur, vous pouvez choisir parmis les monstres suivants:")
print("lequel vous semble a votre mesure?")
for type in monstres.keys():
    prompt = "monstre?"            
for type, fp in monstres.items():
    result = input(prompt)
    if result == str(type):
        pv_ennemi = fp * 100
        force_ennemi = fp * 5
    print("très bien ! vous allez donc vous battre contre un " + str(type) + " ,un ennemi à " + str(pv_ennemi) + " points de vie.")

coup = force_ennemi
dv_perdus = 0

while pv_ennemi > 0:
    print("Que voulez vous faire?")
    print(" 1 - attaquer")
    print(" 2 - boire une potion ")
    choice = input("Saisissez votre choix")
    if choice == '1':
        pv_ennemi -= forcej
        dv_perdus += forcej
        print("il reste " + str(pv_ennemi) + " points de vie à l'ennemi")
        if dv_perdus >= pv_ennemi/10:
            dv_perdus = 0
            pvj -= coup
            print("l'ennemi attaque, il vous reste" + str(pv) + " points de vie")
    if choice == '1':
        pvj += pv_potion
    if pvj > 100:
        pvj = 100
    print("vous avez récupéré " + str(pv_potion) + " points de vie. vous en avez désormais " + str(pv) + ".")
    if pvj <= 0:
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
        if pv > 100:
            pv = 100
        print("vous avez récupéré " + str(pv_potion) + " points de vie. vous en avez désormais " + str(pv) + ".")
    if choice == '2':
        loot = random.choice(loot_ennemi)
        print("vous avez récupérer sur votre ennemi une " + str(loot) + ".")
    if choice == '3':
        pv_ennemi = 200
        print("vous décidez de quitter la pièce")

del monstres[monstre]



