import turtle
from turtle import *

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed(speed=0)
t1.shape(name='turtle')
colormode(255)

dist = 1
step = 0.5
angle = 90
red = 255
green = 0
blue = 0

while True:
    t1.color(red, green, blue)
    t1.right(angle)
    t1.forward(dist)
    dist += step
    red += 10
    if red >= 255:
        red = 0
        green += 10

    if green >= 255:
        green = 0
        blue += 10

    if blue >= 255:
        blue = 0
    angle = (angle + step) % 360
# turtle.exitonclick()

# t2.speed(3)
# t2.shape('circle')
# t2.back(100)
