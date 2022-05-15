from logging import getLogger
from core.command_parser import parse_cmd, parse_place_params
from core.toyrobot import ToyRobot
from settings import Command, TABLE_SIZE_X, TABLE_SIZE_Y, HELP_FILE


log = getLogger(__name__)


def interactive_runner():
    _show_intro()
    bot = ToyRobot()
    cmd = ''
    while cmd not in ['quit', 'exit', 'q', 'x']:
        cmd = input('Enter command:').strip().lower()
        command, params = parse_cmd(cmd)
        if not command:
            continue
        elif command in ['help', '?', 'sos', 'rescue']:
            _show_help(HELP_FILE)
        elif command == Command.PLACE.value:
            bot.dispatch(command, *params)
        else:
            bot.dispatch(command)
    print('k, bye!')


def _show_intro():
    print()
    print('Running in interactive mode...')
    print('Enter "help" to show the different commands and their syntax.')


def _show_help(help_file):
    with open(help_file, 'r') as help_file:
        help_text = help_file.read().format(TABLE_SIZE_X=TABLE_SIZE_X, TABLE_SIZE_Y=TABLE_SIZE_Y)
        print(help_text)
