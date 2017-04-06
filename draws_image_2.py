import turtle
import math
import random

wn = turtle.Screen()

William = turtle.Turtle()
William.speed(0)
William.shape('classic')

William.right(140)
William.forward(-45)

for i in range(96):
    for i in range(7):
        for i in range(2):
            William.color("black")
            William.forward(100)
            William.left(40)
            William.forward(i*4)
            William.left(60)
            William.forward(i*1.2)
            William.left(170)
            William.forward(i*1.5)
            William.forward(i*7)
        William.left(120)
        William.left(120)
        William.color("orange")
        William.forward(i * 2)
        William.left(100)
        William.forward(i * 4)
        William.left(35)
        William.forward(i*1.5)
        William.left(145)
        William.forward(i*1.5)
        William.left(120)
        William.left(130)
        
    William.color("yellow")

    William.forward(i * 17)
    William.left(250)
    William.forward(i * 14)

    William.left(145)
    William.forward(i*2)
    William.left(120)
    William.left(140)
    William.forward(15)
    William.left(12)
    William.left(20)
