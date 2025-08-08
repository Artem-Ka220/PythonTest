'''
Согласно одному древнему поверью,
трёхзначное число считается красивым,
если сумма его минимальной и максимальной цифр
равна оставшейся цифре умноженной на 2.

Напишите программу, которая проверяет, является ли число красивым.

Формат вв ода
Одно трёхзначное число

Формат вывода
YES — если число красивое, иначе — NO
'''

number = int(input())

one = number // 100
two = number // 10 % 10
three = number % 10

numbers = [one, two, three]
numbers_sort = sorted(numbers)

if numbers_sort[0] + numbers_sort[2] == numbers_sort[1] * 2:
    print('YES')
else:
    print('NO')
