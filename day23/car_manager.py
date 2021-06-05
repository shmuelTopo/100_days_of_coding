import turtle
from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "green", "blue", "purple", "yellow"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 350

MODE_TESLA = False


LINE_SPACE = 30
LANES = range(-210, 235, LINE_SPACE * 2)


def get_random_distance():
    return randint(100, 500)


def create_lines(y_position):
    x_cor = STARTING_X
    while x_cor > -400:
        line = Turtle('square')
        line.penup()
        line.goto(x_cor, y_position)
        line.shapesize(stretch_wid=0.3, stretch_len=2)
        line.color('white')
        x_cor -= 100


class Lane:
    def __init__(self, starting_y):
        self.starting_y = starting_y
        self.cars = []
        self.add_car()
        self.car_distance = get_random_distance()
        create_lines(self.starting_y - LINE_SPACE)

    def add_car(self):
        car = Turtle(f'square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()

        # If cars list is empty add the new car to the starting y and starting x +  the random car distance
        if not self.cars:
            car.goto(STARTING_X - get_random_distance(), self.starting_y)
        else:
            car.goto(STARTING_X, self.starting_y)
        car.color(choice(COLORS))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car: Turtle = car
            car.goto(x=car.xcor() - MOVE_INCREMENT, y=self.starting_y)
            # check if the first car (which is the last one in the list) is more than {car_distance} pixels away
            if self.cars[-1].xcor() + self.car_distance < STARTING_X:
                self.add_car()
                # Update the random car distance
                self.car_distance = get_random_distance()
            if car.xcor() < -400:
                self.cars.remove(car)


class CarManager:
    def __init__(self):
        self.lanes = []
        for lane_y_position in LANES:
            self.lanes.append(Lane(lane_y_position))
        self.create_lines_for_last_lane()

    def create_lines_for_last_lane(self):
        y_position = self.lanes[-1].starting_y + LINE_SPACE
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
