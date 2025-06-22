print("exercice 1")

forgeron = {
    "nom" : "Baldur",
    "commande" : []
}

def ajouterCommande(forg, objet):
    forg["commande"].append(objet)

def affichercommande(forg):
    print("Commandes en attente :")
    for c in forg["commande"]:
        print("-", c)

def annulerCommande(forg, objet):
    if objet in forg["commande"]:
        forg["commande"].remove(objet)
    else:
        print("Objet non trouvé dans la commande.")

while True:
    print("gestion des commandes")
    affichercommande(forgeron)
    print("1 - ajouter un objet")
    print("2 - enlever un objet")
    print("3 - arrêter la commande")
    prompt = input("Que voulez-vous faire?")
    if prompt == "1":
        result1 = input("quel objet voulez-vous ajouter?")
        ajouterCommande(forgeron, result1)
        affichercommande(forgeron)
    if prompt == "2":
        result2 = input("quel objet voulez-vous enlever?")
        annulerCommande(forgeron, result2)
        affichercommande(forgeron)
    if prompt == "3":
        affichercommande(forgeron)
        break

print("exercice 2")

monstres = [{
        "nom": "torg", "type": "gobelinoïde", "pv": 50
    },
    {
        "nom": "grk", "type": "mort-vivant", "pv": 25
    }]

def afficherMonstres():
    print(monstres)

def ajouterMonstre(nom, type, pv):
    monstres.append({"nom": nom, "type": type, "pv": pv})

def taperMonstre(nom, degats):
    for ennemi in monstres:
        if ennemi["nom"] == nom:
            ennemi["pv"] -= degats
            print(f"{nom} a perdu {degats} PV, il lui reste {ennemi['pv']} PV.")
            if ennemi["pv"] <= 0:
                print(f"{nom} est vaincu !")
                monstres.remove(ennemi)
            return
    print("Monstre introuvable.")

while True:
    print("ajoutez un monstre")
    nom1 = input("monstre?")
    type1 = input("son type?")
    pv1 = input("combien de pv?")
    ajouterMonstre(nom1, type1, int(pv1))
    afficherMonstres()
    print("attaquer un monstre")
    choix = input("quel monstre voulez-vous attaquer?")
    attaque = input("a combien est la puissance de votre attaque?")
    taperMonstre(choix, int(attaque))
