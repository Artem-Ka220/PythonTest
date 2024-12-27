vowels = ['a', 'e', 'i', 'o', 'u']
newVowels = set(vowels)
word = input('Provide a word to search for vowels ')
same = newVowels.intersection(set(word))
print(same)
