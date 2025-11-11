# 🧠 Cours — Python Core 1

Objectif du jour :

> **Poser les fondations solides pour écrire un code propre, logique et structuré.**

Tu vas apprendre et pratiquer :

| Thème       | Ce que tu vas maîtriser                  |
| ----------- | ---------------------------------------- |
| Variables   | Base de tout code                        |
| Types       | int, float, str, bool, list, tuple, dict |
| Fonctions   | Architecture du code                     |
| Conditions  | Logique + algorithmes simples            |
| Boucles     | Automatisation                           |
| Print/debug | Pensée développeur                       |

---

## 📌 1) **Variables & Types**

Une variable = une "boîte" qui contient une donnée.

```python
name = "Alex"        # string
age = 25             # int
temperature = 36.5   # float
is_active = True     # bool
```

### Règles d’or

* snake\_case ✅ `user_name`
* pas d'accent, pas d'espace ❌ `nom utilisateur`
* nom clair ✅ `email_list`

---

## 🧮 2) **Opérations**

```python
a = 10
b = 3

print(a + b)  # addition
print(a * b)  # multiplication
print(a / b)  # float division
print(a // b) # division entière
print(a % b)  # modulo (reste)
print(a ** b) # puissance
```

---

## 🧩 3) **Conditions**

```python
age = 18

if age > 18:
    print("Adulte")
elif age == 18:
    print("Juste majeur")
else:
    print("Mineur")
```

Indente **4 espaces** (très important).

---

## 🔁 4) **Boucles**

### `for`

```python
for number in [1,2,3]:
    print(number)
```

### `while`

```python
x = 3
while x > 0:
    print(x)
    x -= 1
```

---

## 📦 5) **Structures**

### Liste (modifiable)

```python
fruits = ["pomme", "banane"]
fruits.append("orange")
```

### Tuple (non modifiable)

```python
coords = (12.5, 45.3)
```

### Dictionnaire (clé → valeur)

```python
user = {"name": "Alex", "age": 25}
print(user["name"])
```

---

## 🛠️ 6) **Fonctions**

```python
def greet(name):
    return f"Bonjour {name}"
```

Bonne pratique = **1 fonction = 1 rôle**

---

## 🐛 7) Debug & Print

Toujours vérifier ton code :

```python
print(variable)
type(variable)
```
