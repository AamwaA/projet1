from quetes import quetes_disponibles
from joueur import joueur1
from utils import demander_choix

def afficher_et_choisir_quetes(joueur):
    print("Quêtes disponibles :")
    for i, objet in enumerate(quetes_disponibles, 1):
        print(f"  {i}. {objet}")
    choix = demander_choix("Quelle quête choisissez vous?", 1, len(quetes_disponibles)) - 1
    quete_choisie = quetes_disponibles[choix]
    joueur.quetes_en_cours.append(quete_choisie)
    print(f"Vous avez accepté la quête : {quete_choisie.titre}")
    
def accomplir_quete(joueur):
    if not joueur.quetes_en_cours :
        print("vous n'avez pas de quête en cours")
        return
    for i, objet in enumerate(joueur.quetes_en_cours, 1):
        print(f"  {i}. {objet}")
    choix = demander_choix("Quelle quête choisissez vous?", 1, len(joueur.quetes_en_cours)) - 1
    quete_choisie = joueur.quetes_en_cours[choix]
    print(quete_choisie.terminer())
    joueur.quetes_en_cours.remove(quete_choisie)
    joueur.gagner_or(quete_choisie.recompense)

afficher_et_choisir_quetes(joueur1)
afficher_et_choisir_quetes(joueur1)

joueur1.afficher_infos()

accomplir_quete(joueur1)

joueur1.afficher_infos()