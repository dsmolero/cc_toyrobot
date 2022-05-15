from logging import getLogger
from core.command_parser import parse_cmd, parse_place_params
from core.runners.common import Runner
from core.toyrobot import ToyRobot
from settings import Command, TABLE_SIZE_X, TABLE_SIZE_Y, HELP_FILE, HELP_COMMANDS


log = getLogger(__name__)
EXIT_COMMANDS = ['quit', 'exit', 'q', 'x']


def interactive_runner():
    _show_intro()
    runner = Runner(cmd_generator)
    runner.run()
    print('k, bye!')


def cmd_generator():
    cmd = ''
    while cmd.strip().lower() not in EXIT_COMMANDS:
        cmd = input('Enter command:')
        yield cmd


def _show_intro():
    print()
    print('Running in interactive mode...')
    print('Enter "help" to show the different commands and their syntax.')
