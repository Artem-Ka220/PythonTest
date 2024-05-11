import re

your_sentence_text = input('Введите ваше предложение: ')
print(your_sentence_text)

plist = []

for i in your_sentence_text.split():
    if i.lower() not in plist:
        plist.append(i.lower())

print(plist)

count = 0
for i in plist:
    count += 1

print(count)
