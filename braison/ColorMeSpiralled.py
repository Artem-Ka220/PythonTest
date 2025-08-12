# ColorMeSpiralled.py

import turtle
t = turtle.Pen()
colors = ['red', 'blue', 'pink', 'green', 'yellow', 'aqua', 'purple', 'brown']
number = int(turtle.numinput('Количество цветов', 'Сколько цветов будем указывать (1 - 8)?', 4, 1, 8))
name = turtle.textinput('Введите своё имя.', 'Как вас зовут? ')
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x % number])
    t.penup()
    t.forward(x * number)
    t.pendown()
    t.write(name, font=('Arial', int((x + number) / number), 'bold'))
    t.left(200)
