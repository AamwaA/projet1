class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = 1
        self.pv = 100
        self.or_disponible = 0
        self.inventaire = []
        self.quetes_en_cours = []

    def afficher_infos(self):
        print("=== STATUT DU PERSONNAGE ===")
        print(f"Nom      : {self.nom}")
        print(f"PV       : {self.pv}/100")
        print(f"Or       : {self.or_disponible}")
        print("Quêtes en cours :")
        for i, objet in enumerate(self.quetes_en_cours, 1):
            print(f"  {i}. {objet}")
        print("Inventaire :")
        for i, objet in enumerate(self.inventaire, 1):
            print(f"  {i}. {objet}")
        print("============================")
    
    def gagner_or(self, montant):
        self.or_disponible += montant
        print(f"{self.nom} a gagné {montant} pièces d'or.")

joueur1 = Joueur("Aria")

joueur1.afficher_infos()