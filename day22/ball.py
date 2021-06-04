from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 4
        self.y_move = 4

    def move(self, x_move_amount, y_move_amount):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()


