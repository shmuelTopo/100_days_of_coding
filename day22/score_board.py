from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.penup()
        self.goto(0, 200)
        self.pendown()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score}       {self.r_score}', False, 'center', ('ariel', 60, 'normal'))

    def increase_left_score(self):
        self.l_score += 1
        self.update_score()

    def increase_right_score(self):
        self.r_score += 1
        self.update_score()

