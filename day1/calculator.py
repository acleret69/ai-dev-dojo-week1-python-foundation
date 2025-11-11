"""Mission finale du jour

Crée un mini programme terminal :
Calculatrice basique
addition
soustraction
multiplication
division

Utilise :
variables
input()
conditions
fonctions"""


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


def get_user_choice():
    print("")
    print("\n--- Nouvelle opération ---")
    print("Choisis une opération:")
    print("1: Addition")
    print("2: Soustraction")
    print("3: Multiplication")
    print("4: Division")
    print("0: Quitter")

    choice = input("Ton choix (1/2/3/4) ou 0 pour quitter l'application:  ")

    if choice == "0":
        return choice, None, None

    float_a = float(input("Nombre 1: "))
    float_b = float(input("Nombre 2: "))

    return choice, float_a, float_b


choice, float_a, float_b = get_user_choice()
while choice != "0":
    if choice == "1":
        print(add(float_a, float_b))
    elif choice == "2":
        print(subtract(float_a, float_b))
    elif choice == "3":
        print(multiply(float_a, float_b))
    elif choice == "4":
        print(divide(float_a, float_b))
    else:
        print("Option inconnue")

    choice, float_a, float_b = get_user_choice()
