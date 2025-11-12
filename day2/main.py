from math_utils import add, divide, multiply, subtract

while True:
    # conceptions des options possible du menu
    options = {
        "1": ("Addition", add),
        "2": ("Soustraction", subtract),
        "3": ("Division", divide),
        "4": ("Multiplication", multiply),
        "0": ("Quitter", None),
    }

    # écriture du menu dans la console
    for key, (label, _) in options.items():
        print(f"{key}: {label}")

    # Récupération du choix
    choice = input("\nTon choix: ")

    # Gestion pour quitter l'application
    if choice == "0":
        print("Au revoir , à la prochaine ;)")
        break

    # Gestion pouroptions inconnue
    if choice not in options:
        print("Option inconnue")
        continue

    # Récupération des numéros
    number_1 = float(input("Numéro 1: "))
    number_2 = float(input("Numéro 2: "))

    # Récupération de la fonction associé et affichage à l'utilisateur
    _, func = options[choice]
    print(f"Résultat de l'opération : {func(number_1, number_2)}")
