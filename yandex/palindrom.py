'''Палиндром - это число, слово, предложение и так далее,
которое и слева-направо, и справа-налево читается одинаково.

А как быстро понять, является ли слово палиндромом?
Написать программу для проверки этого! В этом нам
снова поможет условный оператор.

Формат ввода
Одно четырёхзначное число

Формат вывода
YES если число является палиндромом, иначе — NO.

num = int(input())

if num % 10 == num // 1000:
    num // 10 % 10 == num // 100 % 10
    print('YES')
else:
    print('NO')

num = int(input())

first_number = num % 10
fourth_number = num // 1000
second_number = num // 100 % 10
third_number = num // 10 % 10

if first_number == fourth_number:
    third_number == second_number
    print('YES')
else:
    print('NO')'''

num = int(input())

print('YES' if num // 1000 == num % 10 and
      num // 100 % 10 == num // 10 % 10 else 'NO')
