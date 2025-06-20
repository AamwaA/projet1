class Personnage:
    def __init__(self, nom, pv, energie, degats, inventaire):
        self.nom = nom
        self.pv = pv
        self.energie = energie
        self.degats = degats
        self.inventaire = inventaire

    def afficher_statut(self):  # <- bien à l’intérieur de la classe
            print("=== STATUT DU PERSONNAGE ===")
            print(f"Nom      : {self.nom}")
            print(f"PV       : {self.pv}")
            print(f"Énergie  : {self.energie}")
            print(f"Dégâts   : {self.degats}")
            print("Inventaire :")
            for i, objet in enumerate(self.inventaire, 1):
                print(f"  {i}. {objet}")
            print("============================")

joueur = Personnage(
    nom="Silfer",
    pv=1000,
    energie=100,
    degats=30,
    inventaire=["clé magnétique Alpha", "analyseur biologique", "module de soin"]
)

joueur.afficher_statut()
    