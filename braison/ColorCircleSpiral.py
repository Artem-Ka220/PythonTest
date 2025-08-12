# ColorCircleSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green', 'pink', 'purple', 'orange', 'aqua']
number = int(turtle.numinput('Сколько кругов.', 'Сколько кругов будем рисовать (от 1 до 8)?', 4, 1, 8))
for x in range(200):
    t.pencolor(colors[x % number])
    t.circle(x)
    t.left(360 / number + 1)
    t.width(x * number / 200)
