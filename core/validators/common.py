from logging import getLogger


log = getLogger(__name__)


def check_no_parameters(bot, command, *args, **kwargs):
    if args or kwargs:
        log.error(f'Received unexpected parameters for {command} command; {args}, {kwargs}')
        return False
    return True
