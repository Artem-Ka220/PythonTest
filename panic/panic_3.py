phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

print(' ')

plist_2 = plist[1 : len(plist) - 4 :]
plist_2.pop(2)
plist_2.insert(2, plist_2[-3])
plist_2.pop(4)
plist_2.insert(len(plist_2) - 2, plist_2.pop(-1))
new_frase = ''.join(plist_2)

print(' ')
print(plist)
print(plist_2)
print(new_frase)
