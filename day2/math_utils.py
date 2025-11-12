def add(a: float, b: float) -> float:
    """Retourne la somme de a et b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Retourne la différence entre a et b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Retourne le produit de a et b."""
    return a * b


def divide(a: float, b: float) -> float | None:
    """Retourne le quotient de a et b, ou None si division par zéro."""
    if b == 0:
        print("Erreur : division par zéro interdite.")
        return None
    return a / b
