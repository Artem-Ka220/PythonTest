def search4vowels(word):
    """Returns the vowels found in the specified word."""
    anyWord = set("aeiou")
    return anyWord.intersection(set(word))

yourWord = input("Provide a word to search for vowels: ")
print(search4vowels(yourWord))    
