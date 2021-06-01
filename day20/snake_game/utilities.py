def get_angle(direction: str) -> int:
    """Pass in direction, and get back angle"""
    angle_map = {
        'up': 90,
        'down': 270,
        'left': 180,
        'right': 0.0
    }
    if direction in angle_map:
        return angle_map[direction]
    else:
        raise KeyError(f'Wrong value, you entered {direction}, expecting up/down/left/right')


def get_direction(angle: int) -> str:
    """Pass in angle, and get back direction"""
    direction_map = {
        0: 'right',
        90: 'up',
        180: 'left',
        270: 'down'
    }
    if angle in direction_map:
        return direction_map[angle]
    else:
        raise KeyError(f'Wrong value, you entered {angle}, expecting 0/90/180/270')
