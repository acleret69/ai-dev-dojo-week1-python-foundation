# day2/examples.py
"""Exemples jour 2 — comprehensions, try/except, modules (démonstrations courtes)."""

# ---------- Comprehensions ----------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# carrés
squares = [n**2 for n in numbers]
print("squares:", squares)

# nombres pairs
even_numbers = [n for n in numbers if n % 2 == 0]
print("even_numbers:", even_numbers)

# carrés des impairs
odd_squares = [n**2 for n in numbers if n % 2 != 0]
print("odd_squares:", odd_squares)

# dictionnaire : mot -> longueur
words = ["python", "dojo", "ai", "developer"]
lengths = {w: len(w) for w in words}
print("lengths:", lengths)

# dictionnaire filtré (longueur > 3)
filtered = {w: l for w, l in lengths.items() if l > 3}
print("filtered (len>3):", filtered)


# ---------- try / except ----------
def safe_parse_int(value: str) -> int | None:
    """Essaie de convertir en int, renvoie None si échec."""
    try:
        return int(value)
    except ValueError:
        print(f"safe_parse_int: '{value}' n'est pas un entier valide.")
        return None


print("safe_parse_int('10') ->", safe_parse_int("10"))
print("safe_parse_int('abc') ->", safe_parse_int("abc"))


# ---------- Exemple module import (math_utils) ----------
# Suppose que day2/math_utils.py existe et définit add, subtract, multiply, divide
try:
    from day2.math_utils import add, subtract
except Exception as e:
    print("Import math_utils échoué (exemple) :", e)
else:
    print("add(2,3) =", add(2, 3))
    print("subtract(5,1) =", subtract(5, 1))


# ---------- Docstring example ----------
def greet(name: str) -> str:
    """Retourne une salutation formatée pour `name`."""
    return f"Bonjour {name}"


print(greet("Alex"))
