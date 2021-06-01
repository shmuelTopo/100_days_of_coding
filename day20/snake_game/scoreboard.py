from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', False, 'center', ('ariel', 16, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', ('ariel', 40, 'normal'))


