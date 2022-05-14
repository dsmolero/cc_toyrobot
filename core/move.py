from logging import getLogger
from core.toyrobot import ToyRobot
from settings import Face


log = getLogger(__name__)


def move(bot:ToyRobot):
    if bot.f == Face.NORTH:
        bot.set_y(bot.y + 1)
    elif bot.f == Face.EAST:
        bot.set_x(bot.x + 1)
    elif bot.f == Face.SOUTH:
        bot.set_y(bot.y - 1)
    elif bot.f == Face.WEST:
        bot.set_x(bot.x - 1)
    else:
        log.error(f'invalid bot f value "{bot.f}"')
