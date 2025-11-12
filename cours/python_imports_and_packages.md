# 🧠 Mini Cours — Les Imports et Packages en Python

> Objectif : comprendre en profondeur comment Python charge les modules et packages,
> afin d’éviter les erreurs comme `ImportError: attempted relative import with no known parent package`.

---

## 1️⃣ Qu’est-ce qu’un module ?

Un **module** est un simple fichier Python `.py` que tu peux importer depuis un autre fichier.

### Exemple :
```

math_utils.py
main.py

````

`math_utils.py` :
```python
def add(a, b): return a + b
````

`main.py` :

```python
import math_utils
print(math_utils.add(2, 3))
```

🧩 **Import = exécution du fichier** et mise à disposition de ses fonctions/classes dans ton script.

---

## 2️⃣ Qu’est-ce qu’un package ?

Un **package**, c’est un **dossier contenant un fichier `__init__.py`**.

Ce fichier indique à Python :

> "Ce dossier fait partie d’un ensemble de modules, tu peux l’importer."

### Exemple :

```
my_project/
 ├── math_utils/
 │    ├── __init__.py
 │    ├── add.py
 │    ├── multiply.py
 └── main.py
```

Dans `main.py` :

```python
from math_utils.add import add
print(add(2, 3))
```

✅ Python comprend que `math_utils` est un **package**, et cherche le module `add` dedans.

---

## 3️⃣ Le rôle du `__init__.py`

### Sans ce fichier :

Tu obtiens :

```
ImportError: attempted relative import with no known parent package
```

### Avec ce fichier :

Python sait que le dossier est un **package** et peut charger les sous-modules correctement.

📘 Il peut être vide, ou contenir du code exécuté à l’import.

Exemple :

```python
# math_utils/__init__.py
print("Chargement du package math_utils")
```

Quand tu fais `import math_utils`, ce message s’affiche.

---

## 4️⃣ Les types d’import

### 🔹 Import absolu

C’est la méthode recommandée (claire et stable).

```python
from operations_tool.parser import parse_and_validate
```

➡️ Python part du **point de départ du projet (racine)**.

Avantages :

* Plus lisible
* Plus robuste pour gros projets

---

### 🔹 Import relatif

Utilisé à **l’intérieur d’un package**.

```python
from .parser import parse_and_validate   # même dossier
from ..utils import log                  # dossier parent
```

⚠️ À n’utiliser que **dans des packages** (avec `__init__.py`)
Sinon → `ImportError: no known parent package`

---

## 5️⃣ Comment Python trouve un module

Python cherche dans les chemins listés dans `sys.path` :

```python
import sys
print(sys.path)
```

🧭 Il regarde :

1. le répertoire courant (`.`)
2. le dossier du script exécuté
3. les packages installés (`site-packages`)
4. les chemins déclarés dans la variable d’environnement `PYTHONPATH`

Tu peux ajouter manuellement un chemin :

```python
import sys
sys.path.append("/home/aldrick/workspace/ai-dev-dojo-week1-python-foundations/day2")
```

---

## 6️⃣ Exécution d’un package

### Mauvaise pratique :

```bash
python day2/operations_tool/main.py
```

→ ❌ cause souvent une erreur d’import.

### Bonne pratique :

```bash
cd day2
python -m operations_tool.main operations_tool/sample_files/operations.txt operations_tool/sample_files/results.txt
```

➡️ `-m` indique à Python :

> “Exécute ce module comme un programme, mais garde le contexte de package.”

C’est la **méthode professionnelle** utilisée en production.

---

## 7️⃣ Structure de projet professionnelle

```
my_project/
 ├── day2/
 │    ├── __init__.py
 │    ├── operations_tool/
 │    │    ├── __init__.py
 │    │    ├── parser.py
 │    │    ├── evaluator.py
 │    │    ├── io_utils.py
 │    │    └── main.py
 │    └── cours/
 │         └── python_imports_and_packages.md
 └── README.md
```

✅ Tu peux exécuter :

```bash
python -m day2.operations_tool.main ...
```

---

## 8️⃣ Cas concret : Pourquoi ton erreur est apparue

```
ImportError: attempted relative import with no known parent package
```

💡 Explication :

* Tu as fait un **import relatif** (`from .evaluator import evaluate`)
* Mais tu as lancé ton fichier **directement** (pas comme un module)
* Python ne savait donc pas quel était le “parent package”

✅ Solution :

* Ajouter `__init__.py`
* Lancer avec `python -m` depuis le bon dossier
  ou
* Utiliser des imports absolus si tu lances directement

---

## 9️⃣ Résumé Senior — à retenir

| Concept        | À retenir                                                |
| -------------- | -------------------------------------------------------- |
| Module         | Fichier `.py` importable                                 |
| Package        | Dossier avec `__init__.py`                               |
| Import absolu  | Chemin complet depuis la racine du projet                |
| Import relatif | Chemin à partir du module courant (nécessite un package) |
| `__init__.py`  | Rend un dossier importable                               |
| `-m`           | Exécute un module en gardant le contexte de package      |
| `sys.path`     | Liste des chemins où Python cherche les modules          |

---

## 🔥 Exemple final de test

Depuis `day2/` :

```bash
python -m operations_tool.main operations_tool/sample_files/operations.txt operations_tool/sample_files/results.txt
```

Et dans `main.py` :

```python
from .parser import parse_and_validate
from .evaluator import evaluate
```

✅ Tout fonctionnera.

---

## 🧘‍♂️ Conseil mentor

Quand tu crées un projet Python :

1. Toujours mettre `__init__.py` dans chaque dossier de code
2. Toujours exécuter avec `python -m`
3. Toujours préférer **imports absolus**
4. Toujours organiser ton code en packages logiques
5. Toujours vérifier `sys.path` si tu as des soucis

---

## 🧩 Entraînement

1. Crée un petit package `math_box/` avec `__init__.py`
2. Mets `add.py`, `multiply.py`
3. Crée un `main.py` qui importe et utilise ces fonctions
4. Exécute-le avec `python -m math_box.main`

➡️ Tu auras compris les imports à 100 %.

