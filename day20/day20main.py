from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for seg_num, position in enumerate(starting_position):
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = round(segments[seg_num - 1].xcor())
        new_y = round(segments[seg_num - 1].ycor())
        print(f'new location is {new_x} {new_y}')
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
