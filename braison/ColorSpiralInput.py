import turtle  # Настройка графики turtule

t = turtle.Pen()
turtle.bgcolor('black')

# Настройки списка из любых 8 действительных имен цветов

colors = ['red', 'yellow', 'blue', 'green', 'orange',
          'purple', 'white', 'gray']

# Запросить у пользователя кол - во
# стороно, от 1 до 8,
# кол-во по умолчанию 4

sides = int(turtle.numinput('Сколько сторон',
                            'Сколько сторон вы хотите (1 - 8)?', 4, 1, 8))

# Нарисовать красочную спираль
# с кол - ом сторон по выбору пользователя

for x in range(360):
    t.pencolor(colors[x % sides])
# изменить размер в соответствии с кол - м сторон
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
# изменить размер ручки по мере передвижения во внешнюю сторону
    t.width(x * sides / 200)
