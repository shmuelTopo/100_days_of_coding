import turtle

dir_map = {
    'up': 90,
    'down': 270,
    'left': 180,
    'right': 0.0
}

dir_map2 = {
    90: 'up',
    270: 'down',
    180: 'left',
    0.0: 'right'
}

turtle.register_shape('art/vertical.gif')
turtle.register_shape('art/horizontal.gif')

for horizontal in ['up', 'down']:
    for vertical in ['left', 'right']:
        turtle.register_shape(f'art/{horizontal}_{vertical}.gif')

for part in ['head', 'tongue', 'tail']:
    for direc in dir_map.keys():
        turtle.register_shape(f'art/{part}_{direc}.gif')


def get_pic(heading_dir, heading_into, special_part_of_body=None):

    if special_part_of_body:
        return f'art/{special_part_of_body}_{dir_map2.get(heading_into)}.gif'

    else:
        if heading_dir == heading_into:
            if heading_into in [dir_map.get('left'), dir_map.get('right')]:
                return f'art/vertical.gif'
            else:
                return f'art/horizontal.gif'
        else:
            if heading_dir == dir_map.get('up') or heading_into == dir_map.get('down'):
                horizontal_dir = 'down'
            else:
                horizontal_dir = 'up'
            if heading_dir == dir_map.get('left') or heading_into == dir_map.get('right'):
                vertical_dir = 'right'
            else:
                vertical_dir = 'left'

        return f'art/{horizontal_dir}_{vertical_dir}.gif'


class Snake:
    starting_position = (0, 0)
    starting_heading = 0

    def __init__(self):
        self.segments = []
        self.size = 40

        for _ in range(3):
            self.add_segment()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = round(self.segments[seg_num - 1].xcor())
            new_y = round(self.segments[seg_num - 1].ycor())
            heading_dir = self.segments[seg_num].heading()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].setheading(new_heading)
            self.segments[seg_num].goto(new_x, new_y)
            if seg_num == len(self.segments) - 1:
                self.segments[seg_num].shape(get_pic(heading_dir, new_heading, special_part_of_body='tail'))
            else:
                self.segments[seg_num].shape(get_pic(heading_dir, new_heading))

        first_part = self.segments[0]
        first_part.shape(get_pic(first_part.heading(), first_part.heading(), special_part_of_body='head'))
        self.segments[0].forward(self.size)

    def change_direction(self, direction):
        """Takes a str of direction up/down/left/right"""

        if direction not in dir_map.keys():
            raise ValueError(f'Wrong value, you entered {direction}, expecting up/down/left/right')

        if direction == 'up':
            self.up_key()
        elif direction == 'down':
            self.down_key()
        elif direction == 'left':
            self.left_key()
        else:
            self.right_key()

    def up_key(self):
        print(self.segments[0].heading())
        if self.segments[0].heading() not in [dir_map.get('up'), dir_map.get('down')]:
            self.segments[0].setheading(dir_map.get('up'))

    def down_key(self):
        if self.segments[0].heading() not in [dir_map.get('up'), dir_map.get('down')]:
            self.segments[0].setheading(dir_map.get('down'))

    def left_key(self):
        if self.segments[0].heading() not in [dir_map.get('left'), dir_map.get('right')]:
            self.segments[0].setheading(dir_map.get('left'))

    def right_key(self):
        if self.segments[0].heading() not in [dir_map.get('left'), dir_map.get('right')]:
            self.segments[0].setheading(dir_map.get('right'))

    def add_segment(self):
        new_segment = turtle.Turtle('turtle')
        new_segment.color('white')
        new_segment.penup()
        new_segment.pensize(self.size)

        if not self.segments:
            new_segment.goto(self.starting_position)
            new_segment.setheading(self.starting_heading)
            new_segment.shape(get_pic(new_segment.heading(), new_segment.heading(), special_part_of_body='tongue'))
            self.segments.append(new_segment)

        else:
            new_x = round(self.segments[0].xcor())
            new_y = round(self.segments[0].ycor())
            heading = self.segments[0].heading()
            new_segment.goto(x=new_x, y=new_y)
            new_segment.seth(heading)
            new_segment.shape(get_pic(new_segment.heading(), new_segment.heading(), special_part_of_body='tongue'))
            new_segment.forward(self.size)

            self.segments.insert(0, new_segment)
