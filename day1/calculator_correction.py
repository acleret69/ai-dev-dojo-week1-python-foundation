def add(a: float, b: float):
    return a + b


def subtract(a: float, b: float):
    return a - b


def multiply(a: float, b: float):
    return a * b


def divide(a: float, b: float):
    if b == 0:
        return "Erreur: division par 0"
    return a / b


def calculate():
    while True:
        print("\nChoisis une opération:")
        options = {
            "1": ("Addition", add),
            "2": ("Soustraction", subtract),
            "3": ("Multiplication", multiply),
            "4": ("Division", divide),
            "0": ("Quitter", None),
        }

        for key, (label, _) in options.items():
            print(f"{key}: {label}")

        choice = input("\nTon choix: ")

        if choice == "0":
            print("Au revoir 👋")
            break

        if choice not in options:
            print("Option inconnue")
            continue

        x = float(input("Nombre 1: "))
        y = float(input("Nombre 2: "))

        _, func = options[choice]
        print(func(x, y))


calculate()
