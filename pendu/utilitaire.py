def verifChoix(prompt, liste, errorMessage="réessayez"):
    while True:
        choix = input(prompt)
        if choix in liste:
            return choix
        else:
            print(errorMessage)

