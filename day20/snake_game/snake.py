from utilities import get_angle, get_direction
from segment import Segment


class Snake:
    def __init__(self, segment_size_px=40):
        self._segment_size_px = segment_size_px
        self._segments: list[Segment] = []
        self.initialize_the_snake()

    def head(self):
        return self._segments[0]

    def move(self):
        """move the snake starting from the tail into the position of the segment in front"""

        # first move the tail
        angel_to_move_into = self._segments[-2].heading()
        position = self._segments[-2].position()
        self._segments[-1].move(angel_to_move_into, position, 'tail')

        # loop through the loop in reverse beside the first and last index (head and tail) and move them
        for seg_num in range(len(self._segments) - 2, 0, -1):
            # get the angle to move into from the segment in front
            angel_to_move_into = self._segments[seg_num - 1].heading()
            position = self._segments[seg_num - 1].position()
            self._segments[seg_num].move(angel_to_move_into, position, 'body')

        # finally moving the head
        self._segments[0].move(self._segments[0].heading(), (0, 0), 'head')

    def change_direction(self, direction):
        """Takes a str of direction up/down/left/right"""

        if direction not in ['up', 'down', 'left', 'right']:
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
        if get_direction(self._segments[0].heading()) not in ['up', 'down']:
            self._segments[0].setheading(get_angle('up'))

    def down_key(self):
        if get_direction(self._segments[0].heading()) not in ['up', 'down']:
            self._segments[0].setheading(get_angle('down'))

    def left_key(self):
        if get_direction(self._segments[0].heading()) not in ['left', 'right']:
            self._segments[0].setheading(get_angle('left'))

    def right_key(self):
        if get_direction(self._segments[0].heading()) not in ['left', 'right']:
            self._segments[0].setheading(get_angle('right'))

    def initialize_the_snake(self):
        self._segments.append(Segment((self._segment_size_px * 2, 0), get_angle('right'), 'head', 40))
        self._segments.append(Segment((self._segment_size_px, 0), get_angle('right'), 'body', 40))
        self._segments.append(Segment((0, 0), get_angle('right'), 'tail', 40))

    def add_segment(self):
        head = self._segments[0]
        new_segment = Segment(head.position(), head.heading(), 'tongue', self._segment_size_px)
        new_segment.forward(self._segment_size_px)
        self._segments.insert(0, new_segment)


