import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, starty=20)
screen.bgcolor("light gray")
screen.title('Car Crossing Game')
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

car_manager = CarManager()

# Create the player and add a button listener
game_player = Player()
screen.listen()
screen.onkeypress(fun=game_player.move_up, key='Up')
screen.onkeypress(fun=game_player.move_down, key='Down')

game_is_on = True

loop_count = 0
while game_is_on:
    loop_count += 1
    car_manager.move_lanes()
    time.sleep(0.12)
    screen.update()

screen.exitonclick()
