class Ressource:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite
    
    def afficher(self):
        print("===========")       
        print(f"{self.nom} : {self.quantite}")

    def consommer(self, nombre):
        self.quantite -= nombre
        self.afficher()
    
    def ajouter(self, nombre):
        self.quantite += nombre
        self.afficher()


    