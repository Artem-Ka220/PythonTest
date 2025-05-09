'''Все строки должны быть длиной в 35 символов.

Напишите программу, которая выводит красиво оформленный чек.
Все строки в чеке должны быть длиной ровно 35 символов,
текст выровнен в соответствии с примером.

Формат ввода
Название товара (строка);
цена товара (натуральное число);
вес товара (натуральное число);
количество денег у пользователя (натуральное число).
Товар:                      черешня
Цена:                 3кг * 2руб/кг
Итого:                         6руб
Внесено:                      10руб
Сдача:                         4руб
'''

product_name = input()
cost_product = int(input())
weight = int(input())
debet = int(input())
change = debet - cost_product * weight
cost_product_all = cost_product * weight

print(f'{'Чек':=^35}')
print(f'Товар:{product_name:>29}')
print(f"Цена:{f'{weight}кг * {cost_product}руб/кг':>30}")
print(f'Итого:{weight * cost_product:>26}руб')
print(f'Внесено:{debet:>24}руб')
print(f'Сдача:{debet - weight * cost_product:>26}руб')
print(f'{'':=^35}')
