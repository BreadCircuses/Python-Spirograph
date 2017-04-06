import turtle
import math
import random

wn = turtle.Screen()

Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
Albert.shape('classic')

for i in range(22):
    for i in range(28):
        Albert.color("violet")
        Albert.forward(i*6)
        Albert.left(130)
        Albert.forward(i*2)
        Albert.left(50)

    Albert.color("white")
    Albert.forward(i*9)
    Albert.right(65)
    Albert.forward(i*4)
    Albert.right(120)
    Albert.forward(15)

    Albert.forward(30)
