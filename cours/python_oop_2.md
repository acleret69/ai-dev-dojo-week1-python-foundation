# 🚀 JOUR 4 — OOP 2 : Héritage, Polymorphisme & Architecture Modulaire

### 🎯 Objectifs pédagogiques du jour

À la fin de cette journée tu sauras :

* Ce qu’est **l’héritage** et pourquoi il est indispensable
* Comment éviter la duplication via `super()`
* Comment créer des **sous-calculateurs spécialisés**
* Comment organiser un projet modulaire avec plusieurs classes
* Comment penser **architecture orientée objets** comme un senior
* Concevoir une application extensible (ajout de features sans tout casser)

---

# 📘 PARTIE 1 — Le cours (simple, clair, efficace)

## 1️⃣ Héritage — Le cœur de l’OOP senior

L’héritage = créer une nouvelle classe **qui reprend une partie du comportement d’une autre**, et y ajoute ses propres capacités.

```python
class Animal:
    def parler(self):
        print("Un animal parle.")

class Chien(Animal):
    def parler(self):
        print("Wouf !")
```

### 👍 Pourquoi c’est indispensable ?

* éviter la duplication
* organiser le code
* avoir des “familles” de comportements
* rendre le système extensible
* permettre le polymorphisme

---

## 2️⃣ `super()` — La clé pour réutiliser proprement

```python
class CalculatriceAvancee(Calculator):
    def __init__(self):
        super().__init__()  # on récupère l’historique, le compteur, etc.
```

Si tu oublies `super()`, ta sous-classe ne récupère pas l’état de la classe parente → **grosse erreur débutant**.

---

## 3️⃣ Polymorphisme — Le super-pouvoir

Tu peux utiliser des objets *différents*, mais les manipuler **comme s’ils étaient les mêmes**.

```python
def utiliser_calc(calc):
    print(calc.add(5, 2))

utiliser_calc(Calculator())
utiliser_calc(ScientificCalculator())
```

C’est exactement comme ça qu’on construit :

* des systèmes modulaires
* des API évolutives
* des architectures plug-and-play (plugins)
* des IA agentisées

---

## 4️⃣ Architecture modulaire — Comme un senior

```
oop_calculator/
│── base_calculator.py
│── scientific_calculator.py
│── statistics_calculator.py
│── main.py
```

Chaque fichier = une responsabilité claire.
Tu penses déjà comme ça depuis le Jour 3. 🔥
