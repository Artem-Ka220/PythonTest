def search4vowels(any_words):
    """Display any vowels found in a supplied word"""
    vowels = set('aeiou')
    found = vowels.intersection(set(any_words))
    return bool(found)

your_word = input("Provide a word to search for vowels: ")

print(search4vowels(your_word))
