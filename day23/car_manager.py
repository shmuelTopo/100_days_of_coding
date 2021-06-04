from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300
UP_ANGLE = 90


def get_random_location():
    random_y = choice(range(-230, 230, 50))
    return STARTING_X, random_y


class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []

    def add_car(self):
        car = Turtle('square')
        car.penup()
        car.shapesize(stretch_wid=2, stretch_len=1)
        car.setheading(UP_ANGLE)
        car.goto(get_random_location())
        car.color(choice(COLORS))
        self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car: Turtle = car
            car.goto(x=car.xcor() - MOVE_INCREMENT, y=car.ycor())
            if car.xcor() < -400:
                self.car_list.remove(car)

