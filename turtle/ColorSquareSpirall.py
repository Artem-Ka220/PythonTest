# ColorSquareSpirall.py
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['Red', 'Yellow', 'Blue', 'Green']
for x in range(200):
    t.pencolor(colors[x % 4])
    t.forward(x)
    t.left(91)
