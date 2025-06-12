import math
import random

gold = 0

stock = {
    "potion": {
    "prix": 10,
    "quantité": 5,
}}

def jourDeVente(etal):
    for key, values in stock.items():
        quantité = values.get("quantité")
        while quantité > 0:
            quantité -= 1
            gold += values.get("prix")
        return gold


print("Bonjour! Bienvenue dans votre magasin d'aventurier" \
"")

jourDeVente