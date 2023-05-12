def search4vowels(pharse: str) -> set:
    """Zwraca samogłoski znalezione we frazie podanej jako argument."""
    vowels = set('aeiou')
    return vowels.intersection(set(pharse))


def search4letters(pharse: str, letters: str = 'aeiou') -> set:
    """Zwraca zbiór liter ze zmiennej letters, znalezionych
    w zmiennej pharse."""
    return set(letters).intersection(set(pharse))
