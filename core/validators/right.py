from logging import getLogger
from core.validators import common
from settings import Command


log = getLogger(__name__)


def is_right_command(func):

    def wrapper(bot, command, *args, **kwargs):
        if command != Command.RIGHT:
            return True
        return func(bot, command, *args, **kwargs)
    return wrapper


@is_right_command
def check_no_parameters(bot, command, *args, **kwargs):
    return common.check_no_parameters(bot, command, *args, **kwargs)
