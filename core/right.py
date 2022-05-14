from logging import getLogger
from core.toyrobot import ToyRobot
from settings import Face


log = getLogger(__name__)


def right(bot:ToyRobot):
    if bot.f == Face.NORTH:
        bot.set_f(Face.EAST)
    elif bot.f == Face.EAST:
        bot.set_f(Face.SOUTH)
    elif bot.f == Face.SOUTH:
        bot.set_f(Face.WEST)
    elif bot.f == Face.WEST:
        bot.set_f(Face.NORTH)
    else:
        log.error(f'invalid bot Face value {bot.f}')
