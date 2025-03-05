def search4vowels(word:str) -> set:
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

yourWord = input("Введите ваше слово: ")
print(yourWord)

print(search4vowels(yourWord))

