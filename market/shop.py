import math
import random



gold = 10
lingotAcier = 5

stock = {
    "hache": {
    "prix": 10,
    "quantité": 4,
    "coût": 5,
    },
    "masse": {
    "prix": 5,
    "quantité": 5,
    "coût": 2,
    },
    "épée": {
    "prix": 15,
    "quantité": 3,
    "coût": 8,
    },
}

etal = []

print("Bonjour! Bienvenue dans votre magasin d'aventurier ")
print("vous avez en votre possession les armes suivantes:") 
for type in stock.keys():     
    print("des " + str(type) + "s")
    print("Vous en avez " + str(stock[type]["quantité"]))
    print("et elles coutent chacune " + str(stock[type]["prix"]) + " pièces d'or.")
print("votre petit etal peut contenir cinq place pour mettre en vente votre précieuse marchandise pendant une journée de vente")

'''
def jourDeVente(stock):
    for items, number in stock.items():
            etal.append(random.choices[stock])
        try:
            len(etal) => 5
        else:
            return etal[]

print(etal)
'''
# pour l'instant, on fabrique une liste avec une suite d'append, mais elle ne sort qu'un seul type du dictionnaire
etal.append(random.choice([type]))
etal.append([type])
etal.append([type])
etal.append([type])
etal.append([type])
print(etal)
print(len(etal))

chiffreAffaire = len(etal) * stock[type]["prix"]

print(chiffreAffaire)

print("La journée s'est bien déroulé, vous avez vendu toutes vos marchandises et vous avez gagné " + str(chiffreAffaire) + " pièces d'or")
print("la ville où vous faites vos ventes prend une comission de 10 pour cent de vos ventes quotidiennes")

taxes = chiffreAffaire * 0.1
benefices = chiffreAffaire - taxes
gold += benefices

print("après avoir payé les gardes de la ville, vos bénéfices direct sont de " + str(benefices) + "pièces d'or.")
print("vous avez donc en votre possession " + str(gold) + " pièces d'or.")

'''
test
stock["hache"]["quantité"] -= etal

print("après avoir fait l'inventaire de votre stock, vous notez qu'il vous reste " + str(stock["hache"]["quantité"]) + " hache à vendre")

materiaux = 5
production = materiaux * 3
gold -= production
stock["hache"]["quantité"] += 3

print("Vous passez la nuit à refaire vos stock pour la journée du lendemain.")
print("après déduction du couts de vos matériaux qui s'élèvent à " + str(production) + " pièces d'or")
print(" vous avez été en mesure de fabriquer " + str(stock["hache"]["quantité"]) + " hache à remettre dans vos réserves")
'''