__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    if number < 2:
        return False
    else:
        return True
