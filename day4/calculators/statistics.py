import math

from .base import Calculator


class StatisticsCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def moyenne(self, valeurs: list[float]) -> float:
        result = self._moyenne(valeurs)
        self._save("Moyenne", valeurs, None, result)
        return result

    def mediane(self, valeurs: list[float]) -> float:
        sorted_values = sorted(valeurs)
        len_list = len(valeurs)
        if len(sorted_values) % 2 != 0:
            result = sorted_values[len_list // 2]
        else:
            result = (
                sorted_values[len_list // 2 - 1] + sorted_values[len_list // 2]
            ) / 2
        self._save("Mediane", valeurs, None, result)
        return result

    def variance(self, valeurs: list[float]) -> float:
        result = self._variance(valeurs)
        self._save("Variance", valeurs, None, result)
        return result

    def ecart_type(self, valeurs: list[float]) -> float:
        variance = self._variance(valeurs)
        result = math.sqrt(variance)
        self._save("Ecart_type", valeurs, None, result)
        return result

    def _moyenne(self, valeurs: list[float]) -> float:
        return sum(valeurs) / len(valeurs)

    def _variance(self, valeurs: list[float]) -> float:
        moyenne = self._moyenne(valeurs)
        return sum((x - moyenne) ** 2 for x in valeurs) / (len(valeurs) - 1)

    def __string__(self):
        return "Calculatrice statistique"
