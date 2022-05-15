from enum import Enum
from core.toyrobot import ToyRobot


class Command(Enum):
    PLACE = 'place'
    MOVE = 'move'
    LEFT = 'left'
    RIGHT = 'right'
    REPORT = 'report'


TABLE_SIZE_X = 5
TABLE_SIZE_Y = 5


class Face(Enum):
    NORTH: str = 'north'
    EAST: str = 'east'
    WEST: str = 'west'
    SOUTH: str = 'south'


ToyRobot.command_map = {
    Command.PLACE.value: 'core.place.place',
    Command.MOVE.value: 'core.move.move',
    Command.LEFT.value: 'core.left.left',
    Command.RIGHT.value: 'core.right.right',
    Command.REPORT.value: 'core.report.report',
}

ToyRobot.validators = [
    'core.validators.place.check_3_parameters',
    'core.validators.place.check_x_param',
    'core.validators.place.check_y_param',
    'core.validators.place.check_f_param',
    'core.validators.left.check_no_parameters',
    'core.validators.left.check_bot_must_be_placed',
    'core.validators.right.check_no_parameters',
    'core.validators.right.check_bot_must_be_placed',
    'core.validators.move.check_no_parameters',
    'core.validators.move.check_bot_must_be_placed',
    'core.validators.move.check_will_go_out_of_bounds',
    'core.validators.report.check_no_parameters',
    'core.validators.report.check_bot_must_be_placed',
]

HELP_FILE = 'help-text.txt'
USAGE_FILE = 'usage.txt'
HELP_COMMANDS = ['help', 'h', '?', 'sos', 'rescue']
HELP_PARAMS = HELP_COMMANDS + ['--help', '-h']
EXIT_COMMANDS = ['quit', 'exit', 'q', 'x']
