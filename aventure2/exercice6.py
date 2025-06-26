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

taches = [Tache("coder", 4, "en cours"), Tache("menage", 3, "à faire"), Tache("travail", 5, "terminé")]

for t in taches:
    t.afficher()

choix = input("Quelle tâche voulez vous modifier.")
for t in taches:
    if choix == t.titre:
        choix2 = input("voulez modifier le statut(1) ou la priorité(2) ou les deux(3)?")

        if choix2 == "1":
            nouveau_statut = input("entrez un nouveau statut:")
            t.changer_statut(nouveau_statut)
        
        if choix2 == "2":
            nouvelle_priorité = int(input("Entrez une nouvelle priorité : "))
            t.changer_priorite(nouvelle_priorité)
        
        if choix2 == "3":
            nouveau_statut = input("entrez un nouveau statut:")
            t.changer_statut(nouveau_statut)
            nouvelle_priorité = int(input("Entrez une nouvelle priorité : "))
            t.changer_priorite(nouvelle_priorité)   

for t in taches:
    t.afficher()



