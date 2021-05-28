import random
import turtle
from turtle import Turtle
from random import randint, uniform

tim = Turtle()

'''
# draw a circle
for i in range(4):
    tim.forward(100)
    tim.right(90)
'''
'''
# draw a line with skips
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

'''

'''
for i in range(3, 9):
    r = uniform(0.1, 0.95)
    g = uniform(0.1, 0.95)
    b = uniform(0.1, 0.95)
    tim.pencolor(r, g, b)
    for j in range(i):
        angle = 360 / i
        tim.right(angle)
        tim.forward(50)
'''


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


turtle.colormode(255)

'''
tim.speed('fastest')
tim.pensize(8)
for _ in range(300):
    direction = random.choice([0, 90, 180, 270])
    tim.color(random_color())

    tim.setheading(direction)
    tim.forward(20)
'''


def draw_circles(num_of_circles_in_cycle, size):
    tim.speed("fastest")
    heading = 360 / num_of_circles_in_cycle
    for i in range(num_of_circles_in_cycle + 1):
        tim.circle(size)
        tim.setheading(i * heading)


draw_circles(50, 80)

screen = turtle.Screen()
screen.exitonclick()
