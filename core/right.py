from logging import getLogger
from core.toyrobot import ToyRobot
from settings import Face


log = getLogger(__name__)


def right(bot:ToyRobot):
    try:
        face = bot.f.value
    except AttributeError:
        face = bot.f
    if face == Face.NORTH.value:
        bot.set_f(Face.EAST.value)
    elif face == Face.EAST.value:
        bot.set_f(Face.SOUTH.value)
    elif face == Face.SOUTH.value:
        bot.set_f(Face.WEST.value)
    elif face == Face.WEST.value:
        bot.set_f(Face.NORTH.value)
    else:
        log.error(f'invalid bot Face value {face}')
