import turtle

screen = turtle.Screen()
screen.setup(width=500, height=400)

# turtle object
img_turtle = turtle.Turtle()

# registering the image
# as a new shape
turtle.register_shape('art/tail.gif')

# setting the image as cursor
img_turtle.shape('art/tail.gif')

screen.exitonclick()
