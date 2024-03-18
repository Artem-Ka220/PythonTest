phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

any_list = ["o", "n", "t", "a"]
new_plist = []
for word in plist:
    if(word in any_list):
        new_plist.append(word)
        
print(new_plist)
index = len(new_plist) - 1
new_plist.pop(index)

new_plist.append("p")
new_plist.insert(2," ")

new_word = ''.join(new_plist)
print(new_word)

new_phrase = ''.join(plist)
print(new_phrase)
print(plist)
