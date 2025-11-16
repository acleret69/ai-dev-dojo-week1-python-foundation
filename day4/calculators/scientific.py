import math

from .base import Calculator


class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def puissance(self, a: float, b: float) -> float:
        result = a**b
        self._save("Puissance", a, b, result)
        return result

    def racine(self, a: float) -> float:
        result = math.sqrt(a)
        self._save("Racine", a, None, result)
        return result

    def pourcentage(self, a: float, b: float) -> float:
        result = (a / b) * 100
        self._save("Pourcentage", a, b, result)
        return result

    def factorielle(self, n: int) -> int | None:
        if type(n) != int:
            print("Erreur : le factoriel se fait avec des nombres entier.")
            return None
        result = math.factorial(n)
        self._save("Factorielle", n, None, result)
        return result

    def sinus(self, angle_degrees: float) -> float:
        result = math.sin(math.radians(angle_degrees))
        self._save("Sinus", angle_degrees, None, result)
        return result

    def cosinus(self, angle_degrees: float) -> float:
        result = math.cos(math.radians(angle_degrees))
        self._save("Cosinus", angle_degrees, None, result)
        return result

    def tangente(self, angle_degrees: float) -> float:
        result = math.tan(math.radians(angle_degrees))
        self._save("Tangente ", angle_degrees, None, result)
        return result

    def __string__(self):
        return "Calculatrice scientifique"
