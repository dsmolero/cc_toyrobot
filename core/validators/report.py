from logging import getLogger
from core.toyrobot import ToyRobot
from core.validators import common
from settings import Command, Face, TABLE_SIZE_X, TABLE_SIZE_Y


log = getLogger(__name__)


def is_report_command(func):

    def wrapper(bot, command, *args, **kwargs):
        if command != Command.REPORT:
            return True
        return func(bot, command, *args, **kwargs)
    return wrapper

@is_report_command
def check_no_parameters(bot, command, *args, **kwargs):
    return common.check_no_parameters(bot, command, *args, **kwargs)

def check_bot_must_be_placed(bot:ToyRobot, command:Command, *args, **kwargs):
    ret = True
    if command == Command.PLACE:
        pass
    elif bot.x < 0 or bot.x >= TABLE_SIZE_X:
        ret = False
    elif bot.y < 0 or bot.y >= TABLE_SIZE_Y:
        ret = False
    elif bot.f not in [Face.NORTH, Face.EAST, Face.SOUTH, Face.WEST]:
        ret = False
    if not ret:
        log.error(f'{command} requires the toy robot to be placed on the table')
    return ret