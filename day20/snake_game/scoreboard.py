from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__('square')
        self.shapesize(2, 10)
        self.color("gray")
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.score = 0
        self.write(f'Score: {self.score}', False, 'center', ('ariel', 10, 'normal'))