# import logging as log
from settings import Command, Face, TABLE_SIZE_X, TABLE_SIZE_Y
from logging import getLogger


log = getLogger(__name__)


def is_place_command(func):

    def wrapper(bot, command, *args, **kwargs):
        if command != Command.PLACE:
            return True
        return func(bot, command, *args, **kwargs)
    return wrapper


@is_place_command
def check_3_parameters(bot, command, *args, **kwargs):
    if len(args) + len(kwargs.items()) != 3:
        log.error('place command must have 3 parameters')
        return False
    return True

@is_place_command
def check_x_param(bot, command, *args, **kwargs):
    if len(args) < 1:
        if 'x' not in kwargs:
            log.error('place command requires x parameter')
            return False
        x = kwargs['x']
    else:
        x = args[0]
    if type(x) != int:
        log.error('place command requires x parameter as integer')
        return False
    if x < 0 or x >= TABLE_SIZE_X:
        log.error('place command got a negative value for parameter x')
        return False
    return True

@is_place_command
def check_y_param(bot, command, *args, **kwargs):
    if len(args) < 2:
        if 'y' not in kwargs:
            log.error('place command requires y parameter')
            return False
        y = kwargs['y']
    else:
        y = args[1]
    if type(y) != int:
        log.error('place command requires y parameter as integer')
        return False
    if y < 0 or y >= TABLE_SIZE_X:
        log.error('place command got a negative value for parameter y')
        return False
    return True

@is_place_command
def check_f_param(bot, command, *args, **kwargs):
    if len(args) < 3:
        if 'f' not in kwargs:
            log.error('place command requires f parameter')
            return False
        f = kwargs['f']
    else:
        f = args[2]
    if type(f) != Face:
        log.error('place command requires f parameter as Face')
        return False
    return True
