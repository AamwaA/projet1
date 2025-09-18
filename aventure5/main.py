print("Bonjour joueur" \
"Ce programme va vous permettre d'éditer une feuille de personnage pour le jeu de rôle DD5.5" \
"Veuillez entrer les information de votre personnage et le programme vous éditera un fichier texte résumant les informations")

print("Bonjour aventurier")
nom = input("Quel est votre nom champion?")

print("Enchanté " + nom + "! " + " Très joli nom.")

# Cette fonction verifie que le choix entré par le joueur correspond a une des possibilités envisagées
def verifChoix(prompt, liste, errorMessage="réessayez"):
    while True:
        choix = input(prompt)
        if choix in liste:
            return choix
        else:
            print(errorMessage)