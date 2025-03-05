def search4vowels(word: str) -> set:
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


yourWord = input("Введите ваше слово: ")
print(yourWord)


print(search4vowels(yourWord))


def search4letters(phrase: str, anyStr: str = 'aeiou') -> set:
    """Возвращает гласные из заданного списка, найденные в указанном слове."""
    return set(anyStr).intersection(set(phrase))


yourPhrase = input("Введите ваше слово: ")
yourSet = input("Введите ваш список для поиска совпадений: ")

print(search4letters(yourPhrase, yourSet))

print(search4letters(anyStr='ai', phrase='yourPhrase'))
