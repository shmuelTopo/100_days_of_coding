import random

import colorgram
import turtle
from random import randint, uniform

tim = turtle.Turtle()
turtle.colormode(255)
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for c in colors:
#     rgb_colors.append((c.rgb.r, c.rgb.g, c.rgb.b))
#
#
# print(rgb_colors)

rgb_colors = [(187, 18, 44), (243, 231, 66), (210, 236, 242), (196, 75, 32), (218, 66, 107),
              (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214),
              (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94),
              (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39),
              (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]

tim.hideturtle()
tim.penup()
tim.goto(-250, -200)
tim.showturtle()
tim.speed("fastest")
for i in range(10):
    for j in range(10):
        tim.color(random.choice(rgb_colors))
        tim.dot(15)
        if j < 9:
            tim.forward(40)
    tim.backward(360)

    tim.sety(tim.ycor() + 40)
tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
