# --- Exemple 1 : Classe simple ---
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")


p1 = Personne("Aldrick", 25)
p1.parler()


# --- Exemple 2 : Attributs de classe ---
class Compteur:
    instances = 0

    def __init__(self):
        Compteur.instances += 1


print(Compteur.instances)  # 0
a = Compteur()
b = Compteur()
print(Compteur.instances)  # 2


# --- Exemple 3 : Méthodes spéciales ---
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"{self.nom} - {self.prix}€"


p = Produit("PC Gamer", 1200)
print(p)
