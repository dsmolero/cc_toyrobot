from logging import getLogger
from settings import Face, TABLE_SIZE_X, TABLE_SIZE_Y


log = getLogger(__name__)


def check_no_parameters(bot, command, *args, **kwargs):
    if args or kwargs:
        log.error(f'Received unexpected parameters for {command} command; args={args}, kwargs={kwargs}')
        return False
    return True


def check_bot_must_be_placed(bot, command, *args, **kwargs):
    ret = True
    if bot.x < 0 or bot.x >= TABLE_SIZE_X:
        ret = False
    elif bot.y < 0 or bot.y >= TABLE_SIZE_Y:
        ret = False
    elif bot.f not in [Face.NORTH.value, Face.EAST.value, Face.SOUTH.value, Face.WEST.value]:
        ret = False
    if not ret:
        log.error(f'{command} requires the toy robot to be placed on the table')
    return ret
