joueur = {
    "nom": "Silfer",
    "grade": "Technicien de maintenance",
    "pv": 1000,
    "degats": 30,
    "energie": 100,
    "inventaire": ["clé magnétique Alpha", "analyseur biologique", "module de soin"]
}

drone = {
    "nom": "Drone de sécurité MK-II",
    "pv": 300,
    "degats": 50,
    "inventaire": ["puce de sécurité", "module laser"]
}

def afficher_statut(joueur):
    print("=== STATUT DE MISSION ===")
    print(f"Nom      : {joueur['nom']}")
    print(f"Grade    : {joueur['grade']}")
    print(f"PV       : {joueur['pv']}")
    print(f"Énergie  : {joueur['energie']}")
    print(f"Dégats   : {joueur['degats']}")
    print("Inventaire :")
    for i, objet in enumerate(joueur["inventaire"], 1):
        print(f"  {i}. {objet}")
    print("==========================\n")

def afficher_pv(personnage):
    print(f"il reste {personnage["pv"]} points de vie à: {personnage["nom"]}")

def utiliser_energie(joueur, cout):
    if joueur["energie"] >= cout:
        joueur["energie"] -= cout
    else:
        print("Énergie insuffisante.")
        joueur["energie"] = 0

def ajouter_objet(joueur, objet):
    joueur["inventaire"].append(objet)

def soigner(joueur, soin):
    joueur["pv"] += soin
    if joueur["pv"] > 1000:
        joueur["pv"] = 1000

afficher_statut(joueur)

print("Tu arrives devant la salle de contrôle du Module Alpha.")
print("Une porte blindée te bloque l'accès.")
print("Options disponibles :")
print("1 - Utiliser la clé magnétique")
print("2 - Forcer la porte manuellement")
print("3 - Reculer")

choix1 = input("Que fais-tu ? (1/2/3) ")

if choix1 == "1":
    if "clé magnétique Alpha" in joueur["inventaire"]:
        print("La clé magnétique est reconnue. La porte s'ouvre avec un *bip*.")
        utiliser_energie(joueur, 10)
        print(f"l'action t'as couté de l'energie, il t'en reste: {joueur['energie']}")
    else:
        print("Tu n'as pas de clé magnétique.")
elif choix1 == "2":
    print("Tu essaies de forcer la porte...")
    utiliser_energie(joueur, 30)
    print("C'est difficile, mais tu finis par l'ouvrir.")
    print(f"l'action t'as couté de l'energie, il t'en reste: {joueur['energie']}")
elif choix1 == "3":
    print("Tu recules prudemment. Rien ne se passe.")
else:
    print("Commande inconnue.")

print("la salle de contrôle du Module Alpha est une grande pièce bardée d'intruments électronique")
print("la pièce est plongé dans le noir")
print("Options disponibles :")
print("1 - Explorer la salle")
print("2 - Réparer la console électrique")
print("3 - Ouvrir la porte menant au module Beta")

porte_beta = False
console_electrique = False

while porte_beta == False:
    choix2 = input("Que fais-tu ? (1/2/3) ")
    if choix2 == "1":
        if console_electrique == True:
            ajouter_objet(joueur, "clé magnétique Beta")
            print(f"Dans la salle vous trouvez une clé magnétique avec le nom Beta inscrit dessus")
            utiliser_energie(joueur, 10)
            print(f"l'action t'as couté de l'energie, il t'en reste: {joueur['energie']}")
        else:
            print("vous tattonez dans le noir et heurtez un objet")
            joueur["pv"] -= 100
            afficher_pv(joueur)
    elif choix2 == "2":
        print("Vous trouvez la console électrique sur le mur.")
        utiliser_energie(joueur, 10)
        print("Vous arrivez à remmettre l'électricité dans le module")
        console_electrique = True
        print(f"l'action t'as couté de l'energie, il t'en reste: {joueur['energie']}")
    elif choix2== "3":
        if "clé magnétique Beta" in joueur["inventaire"]:
            print("La clé magnétique est reconnue. La porte s'ouvre avec un *bip*.")
            utiliser_energie(joueur, 10)
            print(f"l'action t'as couté de l'energie, il t'en reste: {joueur['energie']}")
            porte_beta = True
        else:
            print("Tu n'as pas de clé magnétique.")

afficher_statut(joueur)
print("tu arrives dans le module Beta")
print("une lumière rouge clignotte dans la pièce !")
print("vous voyez arriver par une trappe un drone menaçant")

securité_Beta = True

def recompense(joueur, ennemi):
    print("sur votre ennemi vous trouvez:")
    for i, objet in enumerate(ennemi["inventaire"]):
        print(f"{i+1}. {objet}")
    for objet in ennemi["inventaire"]:
        ajouter_objet(joueur, objet)

def lancer_combat(joueur, ennemi):
    print("vous allez combattre un:")
    print(ennemi)
    afficher_pv(joueur)

    while joueur["pv"] > 0 and ennemi["pv"] > 0:
        print("Options disponibles :")
        print("1 - Attaquer")
        print("2 - Utiliser un objet")
        print("3 - Fuir")
        choix = input("Que faites vous ? (1/2/3) ")

        if choix == "1":
            print("Vous attaquez l'ennemi qui réplique en conséquence")
            ennemi["pv"] -= joueur["degats"]
            joueur["pv"] -= ennemi["degats"]
            afficher_pv(joueur)
            afficher_pv(ennemi)
            if joueur["pv"] <= 0:
                print("vous êtes mort")
                return False
            if ennemi["pv"] <= 0:
                recompense(joueur, ennemi)
                utiliser_energie(joueur, 30)
                return True

        elif choix == "2":
            if "module de soin" in joueur["inventaire"]:
                soigner(joueur, 500)
                joueur["inventaire"].remove("module de soin")
                print("Vous utilisez votre module de soin")
                afficher_pv(joueur)
            else:
                print("Vous n'avez plus de quoi vous soigner")

        elif choix == "3":
            print("Vous fuyez et faites machine arrière")
            return False 

victoire = lancer_combat(joueur, drone)
        
if victoire:
    print(f"Vous avez vaincu {drone['nom']}")
    print("Sur lui vous avez trouvé un module laser qui booste vos capacités de combat")
    joueur["degats"] += 50
    securité_Beta = True
else:
    print(f"Vous n'avez pas réussi à vaincre : {drone['nom']}")
    print("Votre corps restera parmi les décombres de la station")

afficher_statut(joueur)    

print("suite")