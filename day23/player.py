from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP_ANGLE = 90


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP_ANGLE)

    def move_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(0, self.ycor() - MOVE_DISTANCE)