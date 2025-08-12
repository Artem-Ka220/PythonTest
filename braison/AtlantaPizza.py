# AtlantaPizza.py
number_of_pizza = eval(input('Сколько пицц вы хотите? '))
cost_per_pizza = eval(input('Сколько стоит пицца? '))

sub_total = number_of_pizza * cost_per_pizza

# подсчитать сумму налога с продаж по ставке 8% от подытога
tax_rate = 0.08
# сохранить8 как дробное значение 0,08

sales_tax = sub_total * tax_rate
total = sales_tax + sub_total

# показать пользователю общую сумму к оплате,
# в том числе налог
print('Полная стоимость $:', total)
print('В том числе $:', sub_total, 'за пиццу и')
print('$', sales_tax, 'налог с продаж.')
