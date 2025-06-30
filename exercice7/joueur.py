class Joueur:
    def __init__(self, nom, energie, inventaire):
        self.nom = nom
        self.energie = energie
        self.inventaire = inventaire
    
    def afficher_statut(self):
        print("==============")
        print(f"vous vous appelez {self.nom}")
        print(f"il vous reste {self.energie} d'énergie")
        for t in self.inventaire:
            t.afficher()
        
    def boire(self):
            for t in self.inventaire:
                if t.nom == "eau":
                    t.consommer(1)
                    self.energie += 10
                    break
                else:
                    print("pas d'eau à boire")
