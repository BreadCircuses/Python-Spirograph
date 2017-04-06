import turtle
import math
import random

wn = turtle.Screen()

Stan = turtle.Turtle()
Stan.speed(0)
Stan.color('white')
Stan.shape('classic')

Stan.left(30)
Stan.forward(-55)

for i in range(100):
    for i in range(15):
        for i in range(8):
            Stan.color("black")
            Stan.forward(70)
            Stan.left(40)
            Stan.forward(i*(-4))
            Stan.left(60)
            Stan.forward(i*(3))
            Stan.left(170)
            Stan.forward(i*1.5)
            Stan.forward(i*7)
        Stan.left(120)

        Stan.color("orange")
        Stan.forward(i * 2)
        Stan.left(100)
        Stan.forward(i * 4)
        Stan.left(35)
        Stan.forward(i*1.5)
        Stan.left(5)
        Stan.forward(i*2.5)
        Stan.right(5)
        Stan.forward(i*1.5)
        Stan.left(120)
        Stan.forward(i*1.5)
        Stan.left(130)
    Stan.color("violet")

    Stan.forward(i * 13)
    Stan.left(350)
    Stan.forward(i * 10)

    Stan.left(145)
    Stan.forward(i*2)
    Stan.left(120)
    Stan.forward(10)
    Stan.left(140)
    Stan.forward(15)
    Stan.left(12)
    Stan.forward(i*6)
    Stan.left(20)