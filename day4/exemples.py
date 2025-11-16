### 1️⃣ Exemple d’héritage simple


class Animal:
    def parler(self):
        print("Un animal émet un son.")


class Chien(Animal):
    def parler(self):
        print("Wouf !")


class Chat(Animal):
    def parler(self):
        print("Miaou !")


### 2️⃣ Exemple d’héritage avec `super()`


class Humain:
    def __init__(self, nom):
        self.nom = nom


class Etudiant(Humain):
    def __init__(self, nom, niveau):
        super().__init__(nom)
        self.niveau = niveau


### 3️⃣ Exemple de polymorphisme


def faire_parler(animal):
    animal.parler()


faire_parler(Chien())
faire_parler(Chat())
