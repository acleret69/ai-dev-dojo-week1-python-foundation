### ✅ Exercice 1 — Comprehensions
# 1. Crée une liste `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]`
# 2. Crée :

#    * `squares` = carrés de chaque nombre
#    * `even_numbers` = nombres pairs
#    * `odd_squares` = carrés uniquement des nombres impairs

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [number**2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_squares = [number**2 for number in numbers if number % 2 != 0]

print(f"squares : {squares}")
print(f"even_numbers : {even_numbers}")
print(f"odd_squares : {odd_squares}")

### ✅ Exercice 2 — Dictionnaire comprehension

# À partir de :
# ```python
# words = ["python", "dojo", "ai", "developer"]
# ```

# Crée un dict : `{mot: longueur}`
# Puis un dict filtré : `{mot: longueur} uniquement si longueur > 3`

# ---

words = ["python", "dojo", "ai", "developer"]
dict_len_worlds = {world: len(world) for world in words}
filter_dict_worlds = {world: len(world) for world in words if len(world) > 3}

### ✅ Exercice 3 — Gestion d’erreurs

# 1. Écris une fonction `safe_divide(a, b)` qui :

#    * essaie la division
#    * gère la division par 0
#    * gère les types invalides (ex: chaînes)
#    * affiche un message clair pour chaque cas


def safe_divide(a, b):
    try:
        return a / b
    except ValueError:
        print("Ce n'est pas un nombre valide.")
    except ZeroDivisionError:
        print("Division par zéro interdite.")
