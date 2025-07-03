class Joueur:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv
    
    def choixnom(self):
        nom = input("Quel est votre pseudo?")
        return nom

    def pvrestant(self):
        self.pv -= 1
        print(f"il vous reste {self.pv} chance")
        
    def safeInput(prompt, errorMessage="réessayez"):
        while True:
            choix = input(prompt)
            if choix is len(1):
                return choix
            else:
                print(errorMessage)

joueur = Joueur("joueur", 5)



