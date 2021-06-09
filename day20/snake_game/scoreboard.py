from turtle import Turtle


def get_high_score() -> int:
    with open('data.txt') as file:
        score: str = file.read()
        return int(score)


def update_high_score(new_high_score: int) -> None:
    with open('data.txt', mode='w') as file:
        file.write(str(new_high_score))


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.score = 0
        self.high_score = get_high_score()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}, High score {self.high_score}', False, 'center', ('ariel', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', ('ariel', 40, 'normal'))
        self.reset()

    def reset(self) -> None:
        if self.score > self.high_score:
            update_high_score(self.score)
            self.high_score = self.score
        self.score = 0
        self.update_score()
