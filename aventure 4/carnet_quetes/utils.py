def demander_choix(prompt, minimum, maximum):
    while True:
        choix = input(prompt)
        try:
            choix = int(choix)
        except ValueError:
            print("veuillez entrez une valeur valide.")
            continue
        if minimum <= choix <= maximum:
            return choix
        else:
            print(f"choisissez une valeur entre {minimum} et {maximum}.")