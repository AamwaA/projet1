import random
import math

print("Bonjour aventurier")
nom = input("Quel est votre nom champion?")

print("Enchanté " + nom + "! " + " Très joli nom.")

# Cette fonction verifie que le choix entré par le joueur correspond a une des possibilités envisagées
def verifChoix(prompt, liste, errorMessage="réessayez"):
    while True:
        choix = input(prompt)
        if choix in liste:
            return choix
        else:
            print(errorMessage)

raceJouable = {
    "humain": {
        "pv": 0,
        "force": 0,
        "dv": 5,
    }, 
    "nain": {
        "pv": 0,
        "force": 0,
        "dv": 7
    }, 
    "elfe": {
        "pv": 0,
        "force": 0,
        "dv": 3
    }
}

exp = 50
niveau = math.floor(exp/10)

for key, value in raceJouable.items():
    dv = value.get("dv")
    pvj = dv*50*niveau
    forcej = (10-dv)*niveau
    value['force'] = forcej
    value['pv'] = pvj


print("il y a trois race dans notre monde")
print("vous avez le choix de jouer :")
for choix in raceJouable.keys():
    print(choix)
print("les nains ont plus de point de vie, mais les elfes infligent plus de dégats")
print("les humains quand à eux, sont un bon entre deux")

prompt = "Race?"
result = verifChoix(prompt, raceJouable, "choisissez une race parmis la liste")
raceChoisie = raceJouable[result]
print("en tant que " + result + ", vous avez " + str(raceChoisie["pv"]) + " points de vie et " + str(raceChoisie["force"]) + " en force.")
print("vous êtes de niveau " + str(niveau))


potion = random.randrange(2, 6, 1)
pv_potion = 50

print("C'est déjà bien et comme je suis sympa je vais vous donner " + str(potion) + " potions de soin.")

monstres = {
    "gobelin": {
        "pv": 0,
        "force": 0,
        "fp": 1,
        },
    "orc": {
        "pv": 0,
        "force": 0,
        "fp": 2,
        },
    "troll": {
        "pv": 0,
        "force": 0,
        "fp": 3,
        }, 
    "géant": {
        "pv": 0,
        "force": 0,
        "fp": 4,
        } 
}

for key, value in monstres.items():
    fp = value.get("fp")
    pv_ennemi = fp*50*niveau
    force_ennemi = fp*niveau
    value['force'] = force_ennemi
    value['pv'] = pv_ennemi

print("Vous voulez maintenant combattre un ennemi")
print("c'est tout à votre honneur")
print("quelle est la menace a votre mesure?")
print("vous pouvez affronter l'un des ennemis suivant, mais gare à vous si vous vous montrez trop hardi...")
for choix in monstres.keys():
    print(choix)

prompt = "monstre?"            
result = verifChoix(prompt, monstres, "choisissez un enemi valide")
ennemiChoisit = monstres[result]
print("très bien ! vous allez donc vous battre contre un " + str(ennemiChoisit) + ".")
print("Un ennemi avec " + str(ennemiChoisit["pv"]) + " points de vie et " + str(ennemiChoisit["force"]) + " en force.")

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
            print("l'ennemi attaque, il vous reste" + str(pvj) + " points de vie")
    if choice == '2':
        if potion == 0:
            print("vous n'avez plus de potion")
            pass
        pvj += pv_potion
        potion -= 1
        print("vous avez récupéré " + str(pv_potion) + " points de vie. vous en avez désormais " + str(pvj) + ".")
    if pvj <= 0:
        print("Vous êtes mort")
        break
    if pv_ennemi <= 0:
        print("vous avez vaincu votre ennemi")
    

pv_potion = random.randrange(10, 101, 10)
loot_ennemi = ("hache", "épée", "armure", "bourse")

inventaire = []

while pv_ennemi <= 0:
    print("Que voulez vous faire?")
    print(" 1 - boire une potion")
    print(" 2 - fouiller votre enemi")
    print(" 3 - partir d'ici")
    choice = input("Saisissez votre choix")
    if choice == '1':
        pvj += pv_potion
        for type, value in raceJouable.items():
            if pvj > 100:
                pvj = 100
        print("vous avez récupéré " + str(pv_potion) + " points de vie. vous en avez désormais " + str(pvj) + ".")
    if choice == '2':
        loot = random.choice(loot_ennemi)
        inventaire.append(loot)
        print("vous avez récupérer sur votre ennemi une " + str(loot) + ".")
    if choice == '3':
        pv_ennemi = 200
        print("vous décidez de quitter la pièce")

print(inventaire)


