# 🏗️ PARTIE 4 — La “Super Calculator Architecture”

On va créer **3 classes** :

## 🔹 1. BaseCalculator (hérite de ton Calculator actuel)

Dans `calculators/base.py`

* add
* subtract
* multiply
* divide
* historique
* stats
* compteur d’opérations
  ✔️ → c’est TON code d’hier

---

## 🔹 2. ScientificCalculator

Dans `calculators/scientific.py`

Fonctions à ajouter :

* `puissance(a, b)`
* `racine(a)`
* `pourcentage(a, b)`
* `factorielle(n)`
* BONUS : trigonométrie (`sin`, `cos`, `tan`)

Toutes les opérations doivent :

* appeler `_save`
* incrémenter le compteur

---

## 🔹 3. StatisticsCalculator

Dans `calculators/statistics.py`

Fonctions à ajouter :

* moyenne d’une liste
* médiane
* variance
* écart-type

---

# 🖥️ PARTIE 5 — Le main.py (menu avec plusieurs modes)

Tu dois permettre à l’utilisateur de choisir :

```
=== CALCULATOR HUB ===
1. Mode Basique
2. Mode Scientifique
3. Mode Statistiques
0. Quitter
```

En fonction du choix, tu instancies :

```python
calc = BaseCalculator()
calc = ScientificCalculator()
calc = StatisticsCalculator()
```

---