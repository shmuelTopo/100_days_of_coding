from random import choice
from turtle import Turtle

import settings


def create_lines(y_position):
    x_cor = settings.starting_x
    while x_cor > -400:
        line = Turtle('square')
        line.penup()
        line.goto(x_cor, y_position)
        line.shapesize(stretch_wid=settings.lane_stretch_wid, stretch_len=settings.lane_stretch_len)
        line.color('white')
        x_cor -= 100


class Lane:
    def __init__(self, starting_y):
        self.starting_y = starting_y
        self.cars = []
        self.add_car()
        self.car_distance = settings.get_random_distance()
        create_lines(self.starting_y - settings.line_space)

    def add_car(self):
        car = Turtle(f'square')
        car.shapesize(stretch_wid=settings.car_stretch_wid, stretch_len=settings.car_stretch_len)
        car.penup()

        # If cars list is empty add the new car to the starting y and starting x +  the random car distance
        if not self.cars:
            car.goto(settings.starting_x - settings.get_random_distance(), self.starting_y)
        else:
            car.goto(settings.starting_x, self.starting_y)
        car.color(choice(settings.car_colors))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car: Turtle = car
            car.goto(x=car.xcor() - settings.move_increment, y=self.starting_y)
            # check if the first car (which is the last one in the list) is more than {car_distance} pixels away
            if self.cars[-1].xcor() + self.car_distance < settings.starting_x:
                self.add_car()
                # Update the random car distance
                self.car_distance = settings.get_random_distance()
            if car.xcor() < -400:
                self.cars.remove(car)


class CarManager:
    def __init__(self):
        self.lanes = []
        for lane_y_position in settings.lanes:
            self.lanes.append(Lane(lane_y_position))
        self.create_lines_for_last_lane()

    def create_lines_for_last_lane(self):
        y_position = self.lanes[-1].starting_y + settings.line_space
        create_lines(y_position)

    def move_lanes(self):
        for lane in self.lanes:
            lane.move_cars()

    def get_cars(self) -> list:
        car_list = []
        for lane in self.lanes:
            for car in lane.cars:
                car_list.append(car)
        return car_list
