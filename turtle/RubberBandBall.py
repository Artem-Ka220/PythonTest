# RubberBandBall.py

import turtle
turtle.bgcolor('black')
t = turtle.Pen()
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'pink', 'aqua']
sides = eval(input('Введите количество сторон от двух до восьми: '))

for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + 3)
    t.left(360 / sides + 1)
    t.width(x * sides / 2000)
    t.left(90)
