from logging import getLogger
from core.toyrobot import ToyRobot
from settings import Face


log = getLogger(__name__)


def move(bot:ToyRobot):
    try:
        face = bot.f.value
    except AttributeError:
        face = bot.f
    if face == Face.NORTH.value:
        bot.set_y(bot.y + 1)
    elif face == Face.EAST.value:
        bot.set_x(bot.x + 1)
    elif face == Face.SOUTH.value:
        bot.set_y(bot.y - 1)
    elif face == Face.WEST.value:
        bot.set_x(bot.x - 1)
    else:
        log.error(f'invalid bot f value "{bot.f}"')
