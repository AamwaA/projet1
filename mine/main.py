import random


ore = {
    "pierre": 1, 
    "charbon": 2, 
    "cristal": 5, 
    "fer": 15, 
    "bronze": 30, 
    "argent": 50, 
    "or": 100
}

pioche = random.choices(population=type, cum_weights=[50, 25, 10, 7, 4, 3, 1], k=7)

print(pioche)