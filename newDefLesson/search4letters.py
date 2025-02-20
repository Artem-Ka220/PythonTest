def search4letters(phrase:str,anyStr:str = 'aeiou') -> set:
    """Возвращает гласные из заданного списка, найденные в указанном слову"""
    return set(anyStr).intersection(set(phrase))

 
yourPhrase = input("Введите ваше слово: ")
yourSet = input("Введите ваш список для поиска совпадений: ")

print(search4letters(yourPhrase, yourSet))

print(search4letters('yourPhrase'))
