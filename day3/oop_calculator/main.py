from oop_calculator.calculator import Calculator

calc = Calculator()

while True:
    print("\n=== CALCULATOR OOP ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Historique")
    print("6: Réinitialiser l'historique")
    print("7: Stats")
    print("0. Quitter")

    choice = input("Ton choix: ").strip()

    if choice == "0":
        calc.stats()
        print("👋 Au revoir !")
        break
    if choice == "5":
        calc.history()
        continue
    if choice == "6":
        calc.reset_history()
        continue
    if choice == "7":
        calc.stats()
        continue
    if choice not in ["1", "2", "3", "4"]:
        print("Option invalide.")
        continue

    try:
        a = float(input("Numéro 1: "))
        b = float(input("Numéro 2: "))
    except ValueError:
        print("Entrée invalide.")
        continue

    if choice == "1":
        print(calc.add(a, b))
    elif choice == "2":
        print(calc.subtract(a, b))
    elif choice == "3":
        print(calc.multiply(a, b))
    elif choice == "4":
        print(calc.divide(a, b))
