from math_utils import add, divide, multiply, subtract


def show_menu(options):
    print("\n=== Menu Calculatrice ===")
    for key, (label, _) in options.items():
        print(f"{key}: {label}")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Entrée invalide, veuillez entrer un nombre.")


def main():
    options = {
        "1": ("Addition", add),
        "2": ("Soustraction", subtract),
        "3": ("Division", divide),
        "4": ("Multiplication", multiply),
        "0": ("Quitter", None),
    }

    while True:
        show_menu(options)
        choice = input("\nVotre choix: ").strip()

        if choice == "0":
            print("👋 Au revoir, à la prochaine !")
            break

        if choice not in options:
            print("❌ Option inconnue.")
            continue

        a = get_number("Numéro 1: ")
        b = get_number("Numéro 2: ")
        _, func = options[choice]
        result = func(a, b)

        if result is not None:
            print(f"Résultat de l'opération : {result}")


if __name__ == "__main__":
    main()
