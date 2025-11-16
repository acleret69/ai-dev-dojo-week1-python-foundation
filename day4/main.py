import inspect
from types import MethodType
from typing import Any

from calculators import Calculator

UTILITY_METHODS = {"history", "stats", "reset_history"}


def get_operations_from_calculator(
    calculator_instance: Calculator,
) -> dict[str, MethodType]:
    operations = {}
    for name, method in inspect.getmembers(
        calculator_instance, predicate=inspect.ismethod
    ):
        if name.startswith("_"):
            continue
        if name in UTILITY_METHODS:
            continue
        operations[name] = method
    return operations


def create_calculator_menu(
    all_calculators: list[type[Calculator]],
) -> dict[int, type[Calculator]]:
    return {i + 1: cls for i, cls in enumerate(all_calculators)}


def create_operation_menu(
    operations_name: dict[str, MethodType],
) -> dict[int, MethodType]:
    return {i + 1: method for i, method in enumerate(operations_name.values())}


from typing import get_args, get_origin


def convert_input(user_input: str, expected_type: Any) -> Any:
    # 1. Cas optionnel (ex: float | None)
    if get_origin(expected_type) is None and expected_type is None:
        return None

    # 2. Cas float
    if expected_type is float:
        return float(user_input)

    # 3. Cas int
    if expected_type is int:
        return int(user_input)

    # 4. Cas list[float] / list[int] / etc.
    origin = get_origin(expected_type)
    args = get_args(expected_type)

    if origin is list and args:
        inner_type = args[0]
        return [convert_input(val.strip(), inner_type) for val in user_input.split(",")]

    # Fallback si rien ne matche
    return user_input


def format_type(t):
    if hasattr(t, "__name__"):
        return t.__name__
    return str(t)


# Toutes les calculatrices dispo
all_calculators = [Calculator] + Calculator.__subclasses__()

calculator_menu = create_calculator_menu(all_calculators)

# Menu principal
print("=== CHOISISSEZ UNE CALCULATRICE ===")
for key, calculator in calculator_menu.items():
    print(f"{key}. {calculator.__name__}")
print("0. Quitter")

choice_calculator = int(input("Ton choix: ").strip())
if choice_calculator == 0:
    exit()

calc_class = calculator_menu[choice_calculator]
calc = calc_class()

operations_name = get_operations_from_calculator(calc)

while True:
    operation_menu = create_operation_menu(operations_name)
    print("\n=== MENU DES OPERATIONS ===")
    for key, method in operation_menu.items():
        print(f"{key}. {method.__name__}")
    print("0. Quitter")

    choice = int(input("Ton choix: ").strip())

    if choice == 0:
        calc.stats()
        print("Au revoir !")
        break

    if choice not in operation_menu:
        print("Option invalide.")
        continue

    method = operation_menu[choice]

    # 👉 Rappel : tu dois maintenant analyser la signature
    sig = inspect.signature(method)
    args = []

    for param in sig.parameters.values():
        param_name = param.name
        param_type = param.annotation

        print(f"Entrer la valeur pour {param_name} ({format_type(param_type)}):")

        user_input = input("> ")

        # 🔥 C'est ici que TU dois convertir user_input dans le bon type
        value = convert_input(user_input=user_input, expected_type=param_type)
        args.append(value)

    # Après avoir rempli args :
    result = method(*args)
    print("Résultat :", result)
