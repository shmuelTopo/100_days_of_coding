from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.goto(-200, 250)
        self.pendown()
        self.hideturtle()
        self.level = 0
        self.up_level()

    def up_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', False, 'center', ('ariel', 30, 'normal'))

