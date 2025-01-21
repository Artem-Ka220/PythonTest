def search_for_vowels(word):
    """Выводит гласные, найденные в веденном слове"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
