from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_loc, y_loc):
        super().__init__('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.speed('fastest')
        self.goto(x_loc, y_loc)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down_key_pressed(self):
        self.goto(self.xcor(), self.ycor() - 20)



