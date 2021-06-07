from turtle import Turtle

FONT = ("Courier", 24, "normal")


def get_high_score() -> int:
    with open('high_score.score') as file:
        score: str = file.read()
        return int(float(score))


def update_high_score(new_high_score: int) -> None:
    with open('high_score.score', mode='w') as file:
        file.write(str(new_high_score))


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.score = 0
        self.high_score = get_high_score()
        self.color('green')
        self.up_level(0)

    def up_level(self, time_sec: float):
        if self.level != 0:
            if time_sec > 32:
                bonus = 0
            elif time_sec <= 7:
                bonus = 100
            else:
                bonus = 4 * (30 - time_sec)

            print(f'You score for this level is {100 + bonus}')
            self.score += 100 + bonus
            self.clear()

        self.level += 1
        self.goto(-230, 260)
        self.clear()
        self.write(f'Level: {self.level}', False, 'center', ('ariel', 18, 'normal'))
        self.goto(-100, 260)
        if self.score > get_high_score():
            update_high_score(round(self.score))
            self.high_score = get_high_score()
        self.write(f'Score: {round(self.score)}', False, 'center', ('ariel', 18, 'normal'))
        self.goto(180, 260)
        self.write(f'High Score: {self.high_score}', False, 'center', ('ariel', 18, 'normal'))

    def reset_game(self):
        self.level = 0
        self.score = 0
        self.up_level(0)
