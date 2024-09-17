word = "example"
vowels = {"a", "e", "i", "o", "u"}
found = {}
for letter in word:
    if letter in vowels:
        found[letter] = 1 if letter not in found else found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
