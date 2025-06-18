print("exercice 2")


joueur = {
    "nom": "Thorin",
    "or": 150,
    "inventaire": ["potion", "épée"]
}

print("vous vous appelez ", joueur["nom"])

def afficher_inventaire(joueur):
    print("dans votre bourse vous avez: ", joueur["or"], " pièce d'or dans votre bourse")
    print("dans votre sac, il y a: ", joueur["inventaire"])

afficher_inventaire(joueur)

def ajouter_objet(joueur, objet):
    joueur["inventaire"].append(objet)
    print("vous avez gagnez: ", objet)
    afficher_inventaire(joueur)

def retirer_or(joueur, montant):
    if joueur["or"] >= montant:
        joueur["or"] -= montant
        return True
    else:
        print("vous n'avez pas assez d'or")
        return False

marchand = {
    "bouclier": 50,
    "claymore": 100,
    "relique": 200
}

print("vous faites face à un marchad")
print("voici son étal")
print(marchand)

while True:
    prompt = input("que voulez-vous acheter ? ou quitter pour arrêter")

    if prompt == "quitter":
        break

    if prompt in marchand:
        if retirer_or(joueur, marchand[prompt]):
            ajouter_objet(joueur, prompt)
        else:
            print("Cet objet n'est pas en vente.")


