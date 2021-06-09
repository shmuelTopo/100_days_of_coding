import turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import threading
from playsound import playsound
from pygame import mixer
import time

mixer.init()  # Initialzing pyamge mixer

mixer.music.load('sound/peritune-spook4.wav')  # Loading Music File

mixer.music.play()  # Playing Music with Pygame

screen = turtle.Screen()
screen.setup(width=620, height=620, starty=20)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)
turtle.register_shape(f'art/background.gif')
background = turtle.Turtle('art/background.gif')
background.goto(-4, 4)

snake = Snake()

screen.listen()
screen.onkey(snake.up_key, "Up")
screen.onkey(snake.down_key, "Down")
screen.onkey(snake.left_key, "Left")
screen.onkey(snake.right_key, "Right")


def play_sound(name):
    playsound(name)
    print('done')


def reset_game():
    threading.Thread(target=play_sound, args=['sound/game_over.wav']).start()
    mixer.music.stop()
    time.sleep(3)
    mixer.music.play()
    score_board.reset()
    snake.reset_game()


food = Food()
score_board = ScoreBoard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.18)

    snake.move()
    if snake.head().distance(food) < 10:
        threading.Thread(target=play_sound, args=['sound/eat.wav']).start()
        snake.add_segment()
        score_board.increase_score()

        too_close = True
        while too_close:
            too_close = False
            food.refresh()
            for segment in snake.segments:
                if segment.distance(food) < 10:
                    too_close = True

    # Detect if snake hit a wall
    for cor in [snake.head().xcor(), snake.head().ycor()]:
        if cor < -300 or cor > 300:
            reset_game()

    # Detect if snake hit his tail
    for segment in snake.segments:
        if segment == snake.head():
            pass
        else:
            if segment.distance(snake.head()) < 10:
                reset_game()

screen.exitonclick()
