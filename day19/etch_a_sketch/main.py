from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

heading = 0


def change_heading(num):
    new_heading = tim.heading() + num
    if new_heading > 360:
        new_heading = new_heading - 360
    elif new_heading < 0:
        new_heading = 360 - abs(new_heading)
    return new_heading


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    before = tim.heading()
    tim.setheading(tim.heading() + 10)


def clockwise():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
