### ✅ Exercice 1 — Classe Personne

# Crée une classe `Personne` avec :

# * Attributs : `nom`, `âge`
# * Méthodes :

#   * `se_presenter()`
#   * `vieillir()` → augmente l’âge de 1
#   * `__str__()` → affiche joliment la personne


class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def se_presenter(self) -> None:
        print(f"Bonjour ! Je m'appelle {self.nom} et j'ai {self.age} ans.")

    def vieillir(self) -> None:
        self.age += 1

    def __str__(self) -> str:
        return f"👤 Personne : {self.nom}, {self.age} ans"


# Test
jack = Personne("Jack", 30)
jack.se_presenter()
jack.vieillir()
print(jack)


### ✅ Exercice 2 — Classe CompteBancaire

# Crée une classe avec :

# * `solde` initial
# * `deposer()`, `retirer()`, `afficher_solde()`
# * Si retrait > solde → message d’erreur
# * Bonus : attribut privé `__solde`


class CompteBancaire:
    def __init__(self, solde_initial: float = 0.0):
        self.__solde = solde_initial

    def deposer(self, somme: float) -> None:
        if somme <= 0:
            print("❌ Le montant doit être positif.")
            return
        self.__solde += somme
        print(f"✅ Dépôt de {somme}€ effectué.")

    def retirer(self, somme: float) -> bool:
        if somme > self.__solde:
            print("❌ Solde insuffisant pour ce retrait.")
            return False
        self.__solde -= somme
        print(f"💸 Retrait de {somme}€ effectué.")
        return True

    def afficher_solde(self) -> None:
        print(f"💰 Solde actuel : {self.__solde}€")


# Tests
compte = CompteBancaire(1000)
compte.deposer(500)
compte.afficher_solde()
compte.retirer(1000)
compte.afficher_solde()
compte.retirer(2000)
