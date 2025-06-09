import random

def choisisseurDeMine(chiffre):
    ore = {
        "pierre": chiffre*1, 
        "charbon": chiffre*2, 
        "cristal": chiffre*5, 
        "fer": chiffre*15, 
        "bronze": chiffre*30, 
        "argent": chiffre*50, 
        "or": chiffre*100
}
    return ore

mines = {
    'mine de pierre' : choisisseurDeMine(1),
    'mine de charbon' : choisisseurDeMine(2),
    'mine de fer' : choisisseurDeMine(3)
}

for type in mines.keys():
    print(type)

