import turtle
import random

turtle.register_shape('art/food.gif')


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__('art/food.gif')
        self.shape('art/food.gif')
        self.penup()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_list = range(-280, 280, 40)
        random_y = random.choice(random_list)
        random_x = random.choice(random_list)
        print(f'x {random_x}, y{random_y}')
        self.goto(random_x, random_y)

