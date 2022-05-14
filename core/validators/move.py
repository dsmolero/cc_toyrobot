from settings import Command, Face, TABLE_SIZE_X, TABLE_SIZE_Y
from logging import getLogger


log = getLogger(__name__)


def is_move_command(func):

    def wrapper(bot, command, *args, **kwargs):
        if command != Command.MOVE:
            return True
        return func(bot, command, *args, **kwargs)
    return wrapper


@is_move_command
def check_no_parameters(bot, command, *args, **kwargs):
    if args or kwargs:
        return False
    return True

@is_move_command
def check_out_of_bounds(bot, command, *args, **kwargs):
    if bot.f == Face.NORTH and bot.y >= TABLE_SIZE_Y - 1:
        log.error(f"bot can't move {bot.f}, bot.y={bot.y} TABLE_SIZE_Y={TABLE_SIZE_Y}")
        return False
    if bot.f == Face.EAST and bot.x >= TABLE_SIZE_X - 1:
        log.error(f"bot can't move {bot.f}, bot.x={bot.x} TABLE_SIZE_X={TABLE_SIZE_X}")
        return False
    if bot.f == Face.SOUTH and bot.y <= 0:
        log.error(f"bot can't move {bot.f}, bot.y={bot.y}")
        return False
    if bot.f == Face.WEST and bot.x <= 0:
        log.error(f"bot can't move {bot.f}, bot.x={bot.x}")
        return False
    return True
