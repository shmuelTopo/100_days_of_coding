from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.score = 0
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
        self.goto(-200, 250)
        self.write(f'Level: {self.level}', False, 'center', ('ariel', 30, 'normal'))
        self.goto(150, 250)
        self.write(f'Score: {round(self.score)}', False, 'center', ('ariel', 30, 'normal'))




