from turtle import Screen, Turtle
import time
from snake import Snake
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green yellow")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up_key,  "Up")
screen.onkey(snake.down_key, "Down")
screen.onkey(snake.left_key, "Left")
screen.onkey(snake.right_key, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if random.randint(0, 100) < 5:
        snake.add_segment()

screen.exitonclick()
