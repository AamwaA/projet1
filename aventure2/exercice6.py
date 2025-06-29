class Tache:
    def __init__(self, titre, priorite, statut):
        self.titre = titre
        self.priorite = priorite
        self.statut = statut

    def afficher(self):
        print(f"votre tâche {self.titre}: priorité {self.priorite}.")
        print(f"statut:           {self.statut}")

    def changer_statut(self, nouveau_statut):
        self.statut = nouveau_statut
    
    def changer_priorite(self, nouvelle_priorite):
        if nouvelle_priorite in [1, 2, 3, 4, 5]:
            self.priorite = nouvelle_priorite
        else:
            print("Erreur : la priorité doit être un nombre entre 1 et 5.")
    
class Carnet:
    def __init__(self):
            self.taches = []
        
    def ajouter_taches(self, tache):
            self.taches.append(tache)
        
    def supprimer_taches(self, tache):
            self.taches.remove(tache)
        
    def afficher_toutes(self):
            for t in self.taches:
                t.afficher()
        
    def rechercher_par_titre(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                return tache
        return None


carnet_vide = False

carnet = Carnet()
carnet.ajouter_taches(Tache("manger", 5, "à venir"))
carnet.ajouter_taches(Tache("ménage", 4, "à faire"))
carnet.ajouter_taches(Tache("coder", 3, "en cours"))


while not carnet_vide:
    print("================================")
    print("1 - consulter les tâches")
    print("2 - modifier une tâche")
    print("3 - ajouter une tâche")
    print("4 - supprimer une tâche")
    print("5 - partir")
    print("================================")
    choix = input("Que souhaitez vous faire?")

    if choix == "1":
         carnet.afficher_toutes()
    
    if choix == "2":
            choix = input("quelle tâche voulez-vous modifier?")
            tache = carnet.rechercher_par_titre(choix)
            if tache is None:
                print("Tâche non trouvée.")
            else:
                if tache is not None:
                    choix2 = input("voulez modifier le statut(1) ou la priorité(2) ou les deux(3)?")

                if choix2 == "1":
                    nouveau_statut = input("entrez un nouveau statut:")
                    tache.changer_statut(nouveau_statut)
        
                if choix2 == "2":
                    nouvelle_priorité = int(input("Entrez une nouvelle priorité : "))
                    tache.changer_priorite(nouvelle_priorité)
        
                if choix2 == "3":
                    nouveau_statut = input("entrez un nouveau statut:")
                    tache.changer_statut(nouveau_statut)
                    nouvelle_priorité = int(input("Entrez une nouvelle priorité : "))
                    tache.changer_priorite(nouvelle_priorité) 


    if choix == "3":
         nom = input("quelle tache voulez vous ajouter")
         priorité = int(input("quelle est sa priotité? (1->5)"))
         statut = input("quel est son statut?")
         carnet.ajouter_taches(Tache(nom, priorité, statut))
    
    if choix == "4":
         choix = input("quelle tache voulez-vous supprimer?")
         tache = carnet.rechercher_par_titre(choix)
         if tache is None:
                print("Tâche non trouvée.")
         else:
            carnet.supprimer_taches(tache)

    if choix == "5":
         carnet_vide = True


