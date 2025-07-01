from ressources import Ressource
from joueur import Joueur

eau = Ressource("eau", 1)

joueur = Joueur("tobite", 100, [])

def survivre(joueur, jour):
    while jour < 4:
        print("=================")
        print("1 - faire des recherches")
        print("2 - boire")
        print("3 - ne rien faire")
        choix = input("que voulez-vous faire?")

        if choix == "1":
            print("vous trouvez un puit qui vous permet de récupérer un peu d'eau")
            eau.ajouter(1)
            jour += 1

        if choix == "2":
            print("vous consommer une bouteille d'eau")
            joueur.boire()
            jour += 1

        if choix == "3":
            print("Vous passer votre journée à ne rien faire")
            jour += 1

        else:
            print("veuillez séléctionner un option")

survivre("joueur", 1)


