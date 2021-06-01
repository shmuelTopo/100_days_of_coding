from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up_key,  "Up")
screen.onkey(snake.down_key, "Down")
screen.onkey(snake.left_key, "Left")
screen.onkey(snake.right_key, "Right")

food = Food()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)

    snake.move()
    if snake.head().distance(food) < 10:
        snake.add_segment()
        food.refresh()

screen.exitonclick()
