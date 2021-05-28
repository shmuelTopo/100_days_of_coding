import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class GameTurtle:
    num_of_turtles = 0

    def __init__(self, color, goto_x, goto_y):
        self.color = color
        self.turtle = Turtle('turtle')
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x=goto_x, y=goto_y)
        GameTurtle.num_of_turtles += 1


turtles = [GameTurtle(color=colors[i], goto_x=-230, goto_y=-80 + i * 30) for i in range(len(colors))]

winner_bet = screen.textinput('Make your bet', 'Which turtle will win the race?')

game_over = False
while not game_over:
    for t in turtles:
        t.turtle.forward(random.randint(1, 7))
        if t.turtle.xcor() >= 250:
            if winner_bet == t.color:
                print('You got it right!!')
            else:
                print('You were wrong!!')
            print(f'{t.color} won the game')
            exit()

screen.exitonclick()
