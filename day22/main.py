import turtle
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

screen = turtle.Screen()
screen.setup(width=800, height=600, starty=20)
screen.bgcolor("blue")
screen.title('Pong game')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

# right paddle control
screen.onkeypress(key='Up', fun=r_paddle.go_up)
screen.onkeypress(key='Down', fun=r_paddle.down_key_pressed)

# left paddle control
screen.onkeypress(key='w', fun=l_paddle.go_up)
screen.onkeypress(key='s', fun=l_paddle.down_key_pressed)

# adding the ball
ball = Ball()
y_move = 10
x_move = 10
sleep_time_start = 0.03
sleep_time = sleep_time_start


# adding the score board
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move(x_move_amount=x_move, y_move_amount=y_move)

    ball_x = ball.xcor()
    ball_y = ball.ycor()

    # Detect collision with wall
    if ball_y >= 285 or ball_y <= -285:
        ball.bounce()

    # Detect collision with right and left paddle
    if (ball_x > 330 and ball.distance(r_paddle) <= 60) or (ball_x < -330 and ball.distance(l_paddle) <= 60):
        ball.bounce_paddle()
        sleep_time *= 0.9

    # Detect if Right player is out of boundary
    if ball_x > 350:
        ball.reset_position()
        score_board.increase_left_score()
        sleep_time = sleep_time_start

    # Detect if Left player is out of boundary
    if ball_x < -350:
        ball.reset_position()
        score_board.increase_right_score()
        sleep_time = 0.04


screen.exitonclick()
