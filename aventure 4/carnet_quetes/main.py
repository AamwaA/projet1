from quetes import quetes_disponibles
from joueur import joueur1

def afficher_et_choisir_quetes(joueur):
    print("Quêtes disponibles :")
    for i, objet in enumerate(quetes_disponibles, 1):
        print(f"  {i}. {objet}")
    choix = int(input("Choisissez une quête (1-3) :")) - 1
    quete_choisie = quetes_disponibles[choix]
    joueur.quetes_en_cours.append(quete_choisie)
    print(f"Vous avez accepté la quête : {quete_choisie.titre}")
    
afficher_et_choisir_quetes(joueur1)

joueur1.afficher_infos()
