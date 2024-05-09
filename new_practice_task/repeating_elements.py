your_string = input('Введите вашу строку: ')
print('Вы ввели: ', (your_string))

dict = {}
for i in your_string:
    if i not in dict:
        dict[i] = 0

print(dict)

for i in your_string:
    if i in dict:
        print(i, end = '')
        if int(dict[i]) > 0:
            print('_',dict[i],end = '')
        dict[i] += 1

