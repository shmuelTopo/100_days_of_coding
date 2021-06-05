import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import mixer
from playsound import playsound
import threading

mixer.init()  # Initializing Pygame mixer
mixer.music.load('sound/background.mp3')  # Loading Music File
mixer.music.play()  # Playing Music with Pygame

screen = Screen()
screen.setup(width=600, height=600, starty=20)
screen.bgcolor("light yellow")
screen.title('Car Crossing Game')
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

car_manager = CarManager()

# Create the player and add a button listener
game_player = Player()
screen.listen()
screen.onkeypress(fun=game_player.move_up, key='Up')
screen.onkeypress(fun=game_player.move_down, key='Down')

score_board = Scoreboard()


def play_sound(name):
    playsound(name)
    print('done')


sleep_time = 0.12
game_is_on = True
while game_is_on:
    car_manager.move_lanes()
    time.sleep(0.12)
    for car in car_manager.get_cars():
        if game_player.distance(car) < 25:
            threading.Thread(target=play_sound, args=['sound/smashing.mp3']).start()
            threading.Thread(target=play_sound, args=['sound/game_over.wav']).start()
            game_is_on = False
            mixer.music.stop()
    if game_player.ycor() > 280:
        threading.Thread(target=play_sound, args=['sound/level_up.mp3']).start()
        score_board.up_level()
        game_player.restart_position()
        sleep_time *= 0.9
    screen.update()

screen.exitonclick()
