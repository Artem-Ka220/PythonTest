enterWord = input("Provide a word to search for vowels: ")

def search4vowels(word):
    """Выводит гласные, найденные в указанном слове"""
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for i in found:
        print(i)

search4vowels(enterWord)
