# --- Exercice 1 : List comprehensions ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [n**2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]
odd_squares = [n**2 for n in numbers if n % 2 != 0]

print("squares:", squares)
print("even_numbers:", even_numbers)
print("odd_squares:", odd_squares)


# --- Exercice 2 : Dictionnaire comprehension ---
words = ["python", "dojo", "ai", "developer"]

lengths = {word: len(word) for word in words}
filtered = {word: len(word) for word in words if len(word) > 3}

print("lengths:", lengths)
print("filtered:", filtered)


# --- Exercice 3 : Gestion d’erreurs ---
def safe_divide(a, b):
    """Divise a par b, gère erreurs de type et de division."""
    try:
        return a / b
    except TypeError:
        print("Erreur : les valeurs doivent être numériques.")
    except ZeroDivisionError:
        print("Erreur : division par zéro interdite.")


# Tests
print("safe_divide(10, 2) ->", safe_divide(10, 2))
print("safe_divide(10, 0) ->", safe_divide(10, 0))
print("safe_divide('a', 2) ->", safe_divide("a", 2))
