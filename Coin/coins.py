#На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток,
#которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
#Входные данные:
#На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1,
#если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
#Выходные данные:
#Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

coins = [0, 1, 0, 1, 1, 0]

count_0 = 0
count_1 = 0

for i in coins:
    if i == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_0 < count_1:
    print(count_0)
elif count_0 == count_1:
    print(count_0)
elif count_1 < count_0:
    print(count_1)
else:
    print(0)
    

