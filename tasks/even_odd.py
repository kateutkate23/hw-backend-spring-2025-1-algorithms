__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    if odd_sum == 0:
        return 0
    return even_sum / odd_sum
