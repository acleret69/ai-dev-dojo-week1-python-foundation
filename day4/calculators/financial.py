from .base import Calculator


class FinancialCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def convertir(self, montant: float, taux: float) -> float:
        result = montant * taux
        params = {"montant": montant, "taux": taux}
        self._save("Conversion", params, None, result)
        return result

    def interet_simple(self, capital: float, taux: float, duree: float) -> float:
        result = capital * taux * duree
        params = {"capital": capital, "taux": taux, "duree": duree}
        self._save("Intérêt simple", params, None, result)
        return result

    def interet_compose(self, capital: float, taux: float, periodes: float) -> float:
        result = capital * (1 + taux) ** periodes
        params = {"capital": capital, "taux": taux, "periodes": periodes}
        self._save("Intérêt composé", params, None, result)
        return result

    def tva(self, prix_ht: float, taux_tva: float) -> float:
        result = prix_ht * (1 + taux_tva)
        params = {"prix_ht": prix_ht, "taux_tva": taux_tva}
        self._save("TVA", params, None, result)
        return result

    def __string__(self):
        return "Calculatrice scientifique"
