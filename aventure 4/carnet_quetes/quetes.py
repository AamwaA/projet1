class Quete:
    def __init__(self, titre, recompense):
        self.titre = str(titre)
        self.recompense = int(recompense)
        self.est_terminee = False

    def terminer(self):
        self.est_terminee = True
        return f"La quête '{self.titre}' est terminée !"

    def __str__(self):
        return f"{self.titre} - Récompense : {self.recompense} or - Terminée : {'Oui' if self.est_terminee else 'Non'}"


quetes_disponibles = [
    Quete("Chasser les rats", 10),
    Quete("Livrer une lettre", 15),
    Quete("Explorer les ruines", 20)
]

    
        