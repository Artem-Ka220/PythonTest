# SpiralMyName - печатает цветную спираль из имеени пользователя

import turtle
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green']

# Запрос имени при помощи всплывающего окна textinput()
name = turtle.textinput('Введите своё имя.', 'Как тебя зовут?')

# Нарисовать на экране спираль из имени 100 раз
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()  # не рисовать обычные линии
    t.forward(x * 4)
    t.pendown()  # написать имя, увеличивая каждый раз шрифт
    t.write(name, font=('Arial', int((x + 4) / 4), 'bold'))
    t.left(92)
