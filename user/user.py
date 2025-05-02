user = input('Представьтесь: ')
print('Добрый день, ', user, '.', sep='')

name = input('Назовите своё имя: ')
print(f'Рад приветствовать в python, {name}.')

print(f'{123:0>9}')
print(f'{123:0<9}')
print(f'{123:0^9}')
print('\\')
print(f'{25 ** 0.5:.2f}')

binary_value = '1001'
print(int(binary_value, 2))

cost = float(input())
weight = float(input())
nominal_value = float(input())
print(f'{int(nominal_value - cost * weight)}')

product_name = input()
cost = int(input())
weight = int(input())
amount = int(input())

print('Чек')
print(f'{product_name} - {weight}кг - {cost}руб/кг')
print(f'Итого: {weight * cost}руб')
print(f'Внесено: {amount}руб')
print(f'Сдача: {amount - weight * cost}руб')

num = int(input())
str = input()
print(f'{str}\n' * num)

N = int(input())
your_str = input()
print(f'Я больше никогда не буду писать "{your_str}" \n' * N)

N = int(input())
M = int(input())
print(N // 2 * M)

name = input()
number = int(input())

print(f"Группа №{number // 100}.")
print(f'{number % 10}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number // 10 % 10}.')

number = int(input())
print(f'{number // 100 % 10}{number // 1000}{number % 10}{number // 10 % 10}')
