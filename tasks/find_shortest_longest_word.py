import re

__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    words = re.split(r"[\s,.]+", text)

    shortest = min(words, key=len)
    longest = max(words, key=len)

    return shortest if shortest else None, longest if longest else None
