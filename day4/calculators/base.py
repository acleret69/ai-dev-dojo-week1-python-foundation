class Calculator:
    def __init__(self):
        self.history_log: list = []
        self.__nb_operations: int = 0

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._save("Addition", a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._save("Soustraction", a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._save("Multiplication", a, b, result)
        return result

    def divide(self, a: float, b: float) -> float | None:
        if b == 0:
            print("Erreur : division par zéro.")
            return None
        result = a / b
        self._save("Division", a, b, result)
        return result

    def _save(
        self, operation: str, a: float | list | dict, b: float | None, result: float
    ):
        self.__nb_operations += 1

        if isinstance(a, list):
            a = self._format_values(a)

        if isinstance(a, dict):
            formated = ", ".join(f"{k}={v}" for k, v in a.items())
            self.history_log.append(f"{operation}: {formated} = {result}")
            return

        if b is not None:
            self.history_log.append(f"{operation}: {a} et {b} = {result}")
            return

        self.history_log.append(f"{operation}: {a} = {result}")

    def history(self):
        print("\n📜 Historique des opérations :")
        if not self.history_log:
            print("Aucune opération pour le moment.")
            return
        for entry in self.history_log:
            print("  •", entry)

    def reset_history(self):
        print("\n♻️  Historique réinitialisé avec succès.")
        self.history_log.clear()
        self.__nb_operations = 0

    def stats(self):
        print(f"\nNombre d’opérations effectuées : {self.__nb_operations}")
        if self.history_log:
            print(f"Dernière opération : {self.history_log[-1]}")
        else:
            print("Aucune opération présente dans l'historique")

    def _format_values(self, valeurs):
        if len(valeurs) <= 5:
            return valeurs
        return valeurs[:5] + ["..."]

    def __string__(self):
        return "Calculatrice classique"
