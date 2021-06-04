import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, starty=20)
screen.bgcolor("yellow")
screen.title('Car Crossing Game')
screen.tracer(0)

# Create the player and add a button listener
game_player = Player()
screen.listen()
screen.onkeypress(fun=game_player.move_up, key='Up')
screen.onkeypress(fun=game_player.move_down, key='Down')

car_manager = CarManager()
game_is_on = True

loop_count = 0
while game_is_on:
    loop_count += 1
    if loop_count % 3 == 0:
        car_manager.add_car()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
