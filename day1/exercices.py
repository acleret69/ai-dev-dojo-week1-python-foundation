# Exercice 1 : Carte d’identification
"""Créer : name , age et city
Puis :
Afficher une phrase
Dire si majeur / mineur
"""

name = "john"
age = 30
city = "New York"

print(f"La personne s'appelle {name}, à {age} ans et habite à {city}")

if age > 18:
    print("Adulte")
elif age == 18:
    print("Juste majeur")
else:
    print("Mineur")

# Exercice 2 : Liste + boucle
# Créer une liste de 5 sports puis les afficher.

sports = ["tennis", "badminton", "football", "basketball", "natation"]

for sport in sports:
    print(sport)

"""Exercice 3 : Fonction — analyse mot

Créer une fonction :

```python
def analyze(words):
```

Retourne un dict :

* nombre total de mots
* nombre de mots uniques

Exemple sortie :

```python
{
 "total": 4,
 "unique": 3
}"""


def analyze(words: list[str]):
    return {"total": len(words), "unique": len(set(words))}


print(analyze(["tennis", "badminton", "football", "basketball", "natation", "tennis"]))

"""Challenge — Filtrer pairs

Créer une fonction qui retourne uniquement les nombres pairs d'une liste.
"""


def get_pairs_numbers_four_list(numbers: list[int]):
    return [number for number in numbers if number % 2 == 0]


print(get_pairs_numbers_four_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
