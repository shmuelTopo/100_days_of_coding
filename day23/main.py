import time
from tkinter import TclError
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from pygame import mixer
from playsound import playsound
import threading
from random import choice
import settings

colors = ['cyan', 'bisque', 'light green', 'LemonChiffon2', 'light gray', 'gold', 'plum1', 'wheat2']
colors = colors
mixer.init()  # Initializing Pygame mixer
mixer.music.load('sound/background.mp3')  # Loading Music File
mixer.music.play()  # Playing Music with Pygame

screen = Screen()
screen.setup(width=settings.width, height=settings.height, starty=settings.start_y)
bg_color = choice(colors)
screen.bgcolor(bg_color)
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


def replace_bg():
    global bg_color
    while True:
        new_bg_color = choice(colors)
        if new_bg_color != bg_color:
            screen.bgcolor(new_bg_color)
            bg_color = new_bg_color
            print(bg_color)
            break


game_is_on = True

time_start = time.time()
while game_is_on:
    try:
        car_manager.move_lanes()
        time.sleep(settings.sleep_time)

        # Detect if player got it by a car
        for car in car_manager.get_cars():
            debug_mode = False
            if game_player.distance(car) < settings.distance_too_close and not debug_mode:
                mixer.music.stop()
                threading.Thread(target=play_sound, args=['sound/smashing.wav']).start()
                threading.Thread(target=play_sound, args=['sound/game_over.wav']).start()
                time.sleep(3)
                replace_bg()
                score_board.reset_game()
                settings.reset_game()
                game_player.restart_position()
                mixer.music.play()
                time_start = time.time()

        # Detect if player made it to the top
        if game_player.ycor() > 280:
            print(f'You did the level in {round(time.time() - time_start)} seconds')
            score_board.up_level(time.time() - time_start)
            time_start = time.time()
            threading.Thread(target=play_sound, args=['sound/level_up.wav']).start()
            game_player.restart_position()
            replace_bg()
            settings.level_up()
        screen.update()
    except TclError:
        exit()

time.sleep(3)
screen.bye()
