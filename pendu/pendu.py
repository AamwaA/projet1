import random
from names import names

print("difficulté: facile(1), moyenne(2), difficile(3)")
choixdif = input("quelle difficulté?")
if choixdif == "1":
    mot = random.choice(names["facile"])
if choixdif == "2":
    mot = random.choice(names["moyenne"])
if choixdif == "3":
    mot = random.choice(names["difficile"])


print(mot)

for lettre in mot:
    ltr = input("quelle lettre?")
    if ltr in mot:
        print(ltr)
    else:
        print("cette lettre n'est pas dans le mot")
    
