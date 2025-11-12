# 🧭 Objectifs du Jour 2

| Domaine                          | Objectif                                          |
| -------------------------------- | ------------------------------------------------- |
| List/Dictionnaire comprehensions | Écrire du code concis et élégant                  |
| Gestion d’erreurs (try/except)   | Rendre ton code sûr et stable                     |
| Modules & import                 | Organiser ton projet pro                          |
| Structure projet                 | Préparer le terrain pour des programmes scalables |
| Bonne pratique pro               | Écrire du code lisible pour d’autres devs         |

---

# ⚙️ Préparation

Crée ton dossier :

```
day2/
 ├── notes.md
 ├── examples.py
 ├── exercises.py
 └── cours/
      └── python_core2.py
```

---

# 🧠 COURS — Python Core 2

---

## 🧩 1. Comprehensions — “Le code élégant du senior”

C’est la version **compacte et performante** d’une boucle.

### 🔹 Exemple de boucle classique

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)
```

### 🔹 Version comprehension

```python
squares = [n**2 for n in numbers]
print(squares)
```

---

### 🔹 Filtrage avec condition

```python
even_numbers = [n for n in numbers if n % 2 == 0]
```

### 🔹 Dictionnaire comprehension

```python
words = ["python", "dojo", "mentor"]
lengths = {word: len(word) for word in words}
```

### 🔹 Set comprehension

```python
unique_lengths = {len(word) for word in words}
```

✅ **Avantage :**

* Plus rapide
* Plus lisible (si bien utilisé)
* Réduit les bugs

❌ **Attention :**

* Pas pour des logiques trop complexes
* Lisibilité > concision

---

## ⚠️ 2. Gestion d’erreurs — (try / except)

Les erreurs = inévitables → tu dois les **contrôler** pour éviter les crashs.

### 🔹 Exemple simple

```python
try:
    number = int(input("Entre un nombre : "))
    print(10 / number)
except ValueError:
    print("Ce n'est pas un nombre valide.")
except ZeroDivisionError:
    print("Division par zéro interdite.")
finally:
    print("Fin de l'opération.")
```

### 🔹 Lever une erreur manuellement

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro interdite.")
    return a / b
```

---

## 📦 3. Modules & organisation

Chaque fichier `.py` peut devenir un **module** réutilisable.

### Exemple :

```
project/
 ├── math_utils.py
 └── main.py
```

Dans `math_utils.py`

```python
def add(a, b): return a + b
```

Dans `main.py`

```python
from math_utils import add

print(add(3, 4))
```

✅ Séparer les fonctions par thème = propreté + maintenabilité.

---

## 🧱 4. Structure de projet Python pro

Pour des projets plus grands :

```
src/
 ├── __init__.py
 ├── data/
 ├── models/
 ├── utils/
 ├── main.py
tests/
 └── test_utils.py
```

> Tu apprendras cette organisation plus en détail à la semaine 3 (quand on passera à MLOps & packaging).

---

## 🔍 5. Bonne pratique pro (naming + docstring)

Toujours documenter clairement une fonction :

```python
def greet(name: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {name}"
```

# 🧩 Concept du jour — Résumé façon senior

| Concept            | Résumé                                                        |
| ------------------ | ------------------------------------------------------------- |
| List comprehension | Syntaxe concise pour générer des listes à partir d’itérables  |
| Dict comprehension | Création rapide de dictionnaires à partir de données          |
| try/except         | Gestion d’erreurs contrôlée pour stabilité du code            |
| Modules            | Découper le code pour le rendre réutilisable et maintenable   |
| Bonne pratique     | Noms explicites + fonctions bien documentées = lisibilité pro |

