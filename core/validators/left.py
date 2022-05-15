from logging import getLogger
from core.validators import common
from settings import Command


log = getLogger(__name__)


def is_left_command(func):

    def wrapper(bot, command, *args, **kwargs):
        if command not in [Command.LEFT, Command.LEFT.value]:
            return True
        return func(bot, command, *args, **kwargs)
    return wrapper


@is_left_command
def check_no_parameters(bot, command, *args, **kwargs):
    return common.check_no_parameters(bot, command, *args, **kwargs)


@is_left_command
def check_bot_must_be_placed(bot, command, *args, **kwargs):
    return common.check_bot_must_be_placed(bot, command, *args, **kwargs)
