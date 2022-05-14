from enum import Enum
from core.toyrobot import ToyRobot


class Command(Enum):
    PLACE: str = 'place'
    MOVE: str = 'move'
    LEFT: str = 'left'
    RIGHT: str = 'right'
    REPORT: str = 'report'


TABLE_SIZE_X = 5
TABLE_SIZE_Y = 5


class Face(Enum):
    NORTH: str = 'north'
    EAST: str = 'east'
    WEST: str = 'west'
    SOUTH: str = 'south'


ToyRobot.command_map = {
    Command.PLACE: 'core.place.place',
    Command.MOVE: 'core.move.move',
    Command.LEFT: 'core.left.left',
}

ToyRobot.validators = [
    'core.validators.place.check_3_parameters',
    'core.validators.place.check_x_param',
    'core.validators.place.check_y_param',
    'core.validators.place.check_f_param',
    'core.validators.move.check_no_parameters',
    'core.validators.move.check_out_of_bounds',
]
