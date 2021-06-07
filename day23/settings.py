from random import randint

width = 600
height = 600
start_y = 20

colors = ['cyan', 'spring green', 'bisque']
sleep_time = 0.12
distance_too_close = 30

# For the car_manager
starting_move_distance = 5
move_increment = 10
line_space = 30
lanes = range(-210, 235, line_space * 2)
car_colors = ["red", "orange", "green", "blue", "purple", "yellow"]
starting_x = 350
car_shapesize = (1, 2)

lane_stretch_wid = 0.3
lane_stretch_len = 2
car_stretch_wid = 1
car_stretch_len = 2


def get_random_distance():
    return randint(100, 400)


def level_up():
    global sleep_time
    sleep_time *= 0.9


def reset_game():
    global sleep_time
    sleep_time = 0.12
