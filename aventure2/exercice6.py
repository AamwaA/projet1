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
        
    def rechercher_tache(self, tache):
            if tache in self.taches:
                print(tache)



carnet = Carnet()
carnet.ajouter_taches(Tache("manger", 5, "à venir"))
carnet.ajouter_taches(Tache("ménage", 4, "à faire"))
carnet.ajouter_taches(Tache("coder", 3, "en cours"))

carnet.afficher_toutes()

carnet.rechercher_tache("manger")
