from logging import getLogger

log = getLogger(__name__)


def place(bot, x, y, f):
    bot.set_x(x)
    bot.set_y(y)
    bot.set_f(f)
