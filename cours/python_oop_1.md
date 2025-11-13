# 🧠 Cours Jour 3 — Python OOP 1 : Les bases de la Programmation Orientée Objet

## 🎯 Objectif
Comprendre les **fondements de la POO (Programmation Orientée Objet)** en Python :
- Pourquoi on l’utilise
- Comment créer et manipuler des classes
- La différence entre **méthodes** et **fonctions**
- L’importance du mot-clé `self`
- Comment organiser ton code de manière réutilisable et propre

---

## 1️⃣ Pourquoi la POO ?

Jusqu’ici, tu écrivais des **fonctions isolées** (`add`, `subtract`, etc.).  
Mais à mesure qu’un projet grandit, tu veux :
- **Regrouper** les fonctions liées
- **Conserver un état** (ex: un total, une mémoire)
- **Réutiliser** le code sans copier-coller
- **Faire évoluer** le programme sans tout casser

➡️ La solution : **la POO (Programmation Orientée Objet)**

---

## 2️⃣ Qu’est-ce qu’un objet ?

Un objet = un **concept** du monde réel représenté en code.  
Exemples :
- un `Utilisateur`
- une `Voiture`
- une `Transaction`
- un `Calculateur`

Chaque objet a :
- des **attributs** (ses données)
- des **méthodes** (ses comportements)

---

## 3️⃣ Exemple simple

```python
class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    def demarrer(self):
        print(f"La {self.marque} démarre !")

ma_voiture = Voiture("Tesla", "noire")
ma_voiture.demarrer()
````

🧩 Détails :

* `class Voiture:` → crée une **classe**
* `__init__` → méthode spéciale appelée à la création
* `self` → représente **l’objet lui-même**
* `ma_voiture` → **instance** de la classe

---

## 4️⃣ Méthodes vs Fonctions

| Fonction                           | Méthode                                     |
| ---------------------------------- | ------------------------------------------- |
| Définie **en dehors** d’une classe | Définie **dans** une classe                 |
| Utilisée seule : `print()`         | Appelée sur un objet : `voiture.demarrer()` |

---

## 5️⃣ Attributs d’instance et de classe

```python
class Joueur:
    # attribut de classe
    nb_joueurs = 0

    def __init__(self, nom):
        self.nom = nom
        Joueur.nb_joueurs += 1
```

* `self.nom` → propre à chaque objet
* `nb_joueurs` → partagé entre toutes les instances

---

## 6️⃣ Encapsulation

Principe : **protéger** les données internes d’un objet.
En Python :

* `_attribut` → “interne” (convention)
* `__attribut` → rendu “privé” (renommé en interne)

```python
class CompteBancaire:
    def __init__(self, solde):
        self.__solde = solde

    def deposer(self, montant):
        self.__solde += montant

    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde}€")
```

---

## 7️⃣ Représentation (méthodes spéciales)

Python permet de personnaliser l’affichage des objets :

```python
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€"
```

---

## 8️⃣ Héritage (aperçu)

Une classe peut **hériter** d’une autre :

```python
class Animal:
    def parler(self):
        print("L'animal fait un bruit")

class Chien(Animal):
    def parler(self):
        print("Le chien aboie")

rex = Chien()
rex.parler()
```

---

## 9️⃣ En résumé

| Concept       | Description                  |
| ------------- | ---------------------------- |
| `class`       | Modèle d’un objet            |
| `__init__`    | Initialise l’objet           |
| `self`        | Représente l’objet courant   |
| Attributs     | Données de l’objet           |
| Méthodes      | Actions de l’objet           |
| Héritage      | Réutiliser / étendre le code |
| Encapsulation | Cacher les détails internes  |

---

## 🔥 Mini résumé mental

> **Une classe = un moule.**
> **Un objet = un gâteau.**
> **self = le gâteau en train de se construire.**

---

## 🧘‍♂️ À retenir pour le Dojo :

1. Une classe décrit *ce que c’est* et *ce qu’elle sait faire*
2. Un objet est une *version vivante* de la classe
3. Utilise `self` pour parler **de l’objet lui-même**

---

## ✅ Challenge du jour (projet)

Tu vas transformer ton calculateur de jour 2 en **classe orientée objet** :

* `Calculator` avec :

  * des méthodes `add`, `subtract`, `multiply`, `divide`
  * un attribut `last_result`
  * une méthode `history()` pour afficher les opérations passées
* Un `main.py` qui interagit avec la classe via un menu

➡️ Ce sera ton premier **projet OOP complet.**

# 💪 3. Exercices (`exercises.py`)

### ✅ Exercice 1 — Classe Personne

Crée une classe `Personne` avec :

* Attributs : `nom`, `âge`
* Méthodes :

  * `se_presenter()`
  * `vieillir()` → augmente l’âge de 1
  * `__str__()` → affiche joliment la personne

---

### ✅ Exercice 2 — Classe CompteBancaire

Crée une classe avec :

* `solde` initial
* `deposer()`, `retirer()`, `afficher_solde()`
* Si retrait > solde → message d’erreur
* Bonus : attribut privé `__solde`

---

### ✅ Exercice 3 — Projet : OOP Calculator

Fichiers :

```
day3/oop_calculator/
 ├── __init__.py
 ├── calculator.py
 └── main.py
```

#### `calculator.py`

```python
class Calculator:
    def __init__(self):
        self.history_log = []

    def add(self, a, b):
        result = a + b
        self._save("Addition", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save("Soustraction", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save("Multiplication", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            print("Erreur : division par zéro.")
            return None
        result = a / b
        self._save("Division", a, b, result)
        return result

    def _save(self, operation, a, b, result):
        self.history_log.append(f"{operation}: {a} et {b} = {result}")

    def history(self):
        print("\nHistorique des opérations :")
        for entry in self.history_log:
            print(entry)
```

#### `main.py`

```python
from calculator import Calculator

calc = Calculator()

while True:
    print("\n=== CALCULATOR OOP ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Historique")
    print("0. Quitter")

    choice = input("Ton choix: ").strip()

    if choice == "0":
        print("👋 Au revoir !")
        break
    if choice == "5":
        calc.history()
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
```

---

## 🧱 4. Ce que tu vas maîtriser aujourd’hui

| Compétence            | Objectif                                       |
| --------------------- | ---------------------------------------------- |
| `class` et `__init__` | Créer des objets                               |
| `self`                | Référencer l’instance                          |
| Encapsulation         | Protéger des attributs                         |
| `__str__`             | Rendre les objets lisibles                     |
| Architecture          | Organiser ton projet orienté objet             |
| CLI + objets          | Faire interagir un utilisateur avec une classe |

---

Souhaites-tu que je t’ajoute un **mini module “debug et pensée objet”** (où je t’enseigne comment réfléchir comme un objet, avec analogies et petits exercices mentaux) avant que tu passes à la pratique ?
C’est une étape que les développeurs intermédiaires zappent souvent, mais les seniors la maîtrisent à fond.
