### Exercice 1 — Héritage simple

# Créer :

# * Classe `Vehicule`
# * Classe `Voiture` qui hérite et ajoute `nombre_portes`
# * Classe `Moto` qui hérite et ajoute `cylindree`


class Vehicule:
    def __init__(
        self,
        marque,
        nom,
    ):
        self.marque: str = marque
        self.nom: str = nom


class Voiture(Vehicule):
    def __init__(self, marque, nom, nombre_portes):
        super().__init__(
            marque,
            nom,
        )
        self.nombre_portes: int = nombre_portes

    def __str__(self):
        return f"Ce véhicule est une voiture qui s'appel {self.nom}, de la marque {self.marque} avec {self.nombre_portes} portes"


class Moto(Vehicule):
    def __init__(self, marque, nom, capacite_moteur):
        super().__init__(
            marque,
            nom,
        )
        self.capacite_moteur: int = capacite_moteur

    def __str__(self):
        return f"Ce véhicule est une moto qui s'appelle {self.nom}, de la marque {self.marque} avec {self.capacite_moteur}"


### Exercice 2 — Polymorphisme

# Créer une fonction `decrire(v)` qui fonctionne sur les deux classes.


def decrire(vehicule: Vehicule):
    print(vehicule)


# test

voiture = Voiture(marque="AUDI", nom="TT", nombre_portes=5)
moto = Moto(marque="mercedes", nom="fire", capacite_moteur=150)

decrire(vehicule=voiture)
decrire(vehicule=moto)
