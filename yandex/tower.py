'''
Во времена, когда люди верили в магическую силу чисел,
волшебник Пифуман предал все народы и встал на сторону Зерона.

Теперь, чтобы проникнуть в башни обоих злодеев одновременно,
нужно разделить силу числа, которое защищало нас в дороге.

Для этого возьмём трёхзначное число и составим
из него минимальное и максимальное возможные двухзначные числа.

Формат ввода
Одно трёхзначное число.

Формат вывода
Два защитных числа для каждого отряда, записанные через пробел.
'''

number = int(input())

a = number // 100
b = number // 10 % 10
c = number % 10

word = ''
step = 0
'''
if a < b:
    step = a
    a = b
    b = step
    if b < c:
        step = b
        b = c
        c = step
        if a < b:
            step = a
            a = b
            b = step
else:
    if b < c:
        step = b
        b = c
        c = step
        if b > a:
            step = a
            a = b
            b = step

word = word + str(a) + str(b) + str(c)
a = int(word)

print(a % 100, a // 10)'''

if a > b:
    if b > c:
        if c == 0:
            print(b,c, a,b,sep='')
        else:
            print(c,b, a,b,sep='')
    else:
        if b == 0:
            print(c,b, a,c,sep='')
        else:
            print(b,c, a,c,sep='')
elif b > c:
    if
else:
    if a > c:
        if c == 0:
            print(a,c, b,a,sep='')
        else:
            print(c,a, b,a,sep='')
    else:
        if a == 0:
            print(c,a, b,c,sep='')
        else:
            print(a,c, b,c,sep='')
        
