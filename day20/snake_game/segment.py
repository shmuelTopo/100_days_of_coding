import turtle
from utilities import get_angle, get_direction

# Register all the shape images
turtle.register_shape('art/vertical.gif')
turtle.register_shape('art/horizontal.gif')

for horizontal in ['up', 'down']:
    for vertical in ['left', 'right']:
        turtle.register_shape(f'art/{horizontal}_{vertical}.gif')

for part in ['head', 'tongue', 'tail']:
    for direc in ['up', 'down', 'left', 'right']:
        turtle.register_shape(f'art/{part}_{direc}.gif')


def get_picture(angel_heading_into, angel_coming_from=None, body_part=None):
    """
    pass in the new angle the segment is heading into, in the case the body part is body
    pass in the angle that he came from in the case of 'head' or 'tail' pass in head/tail
    """
    if body_part in ['head', 'tail', 'tongue']:
        return f'art/{body_part}_{get_direction(angel_heading_into)}.gif'

    elif body_part == 'body':
        # if both angles equals each other, it means that the snake is going in a direct line (without turning)
        if angel_coming_from == angel_heading_into:
            if angel_heading_into in [get_angle('left'), get_angle('right')]:
                return f'art/vertical.gif'
            else:
                return f'art/horizontal.gif'

        # if the snake is turning
        else:
            # calculating the horizontal part of the picture if should be up or down
            if angel_coming_from == get_angle('up') or angel_heading_into == get_angle('down'):
                horizontal_dir = 'down'
            else:
                horizontal_dir = 'up'

            # calculating the vertical part of the picture if should be left or right
            if angel_coming_from == get_angle('left') or angel_heading_into == get_angle('right'):
                vertical_dir = 'right'
            else:
                vertical_dir = 'left'

        return f'art/{horizontal_dir}_{vertical_dir}.gif'

    else:
        raise KeyError(f'Wrong value, you entered {body_part}, expecting head/tail/body/tongue')


class Segment(turtle.Turtle):
    def __init__(self, position: tuple, angle: int, body_part: str, size_in_px: int):
        super().__init__()
        self._body_part = body_part
        self._angle = angle
        self._size_in_px = size_in_px
        self.penup()
        self.setheading(angle)
        self.shape(get_picture(angle, angle, body_part))
        self.goto(position)

    def move(self, heading: int, position: tuple, shape: str):
        self.setheading(heading)
        if shape is not 'head':
            self.goto(position)
        else:
            self.forward(self._size_in_px)
        self.shape(get_picture(heading, self._angle, shape))
        self._angle = heading

    def heading(self) -> int:
        return round(super().heading())

    def position(self) -> tuple:
        x = round(self.xcor())
        y = round(self.ycor())
        return x, y
