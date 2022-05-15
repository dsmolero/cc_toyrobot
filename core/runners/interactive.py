from core.toyrobot import ToyRobot
from settings import TABLE_SIZE_X, TABLE_SIZE_Y

def interactive_runner():
    _show_intro()
    bot = ToyRobot()
    cmd = ''
    while cmd not in ['quit', 'exit', 'q', 'x']:
        cmd = input('Enter command:').lower()
        if cmd in ['help', '?', 'sos', 'rescue']:
            _show_help()
    print('k, bye!')


def _show_intro():
    print()
    print('Running in interactive mode...')
    print('Enter "help" to show the different commands and their syntax.')


def _show_help():
    with open('help-text.txt', 'r') as help_file:
        help_text = help_file.read().format(TABLE_SIZE_X=TABLE_SIZE_X, TABLE_SIZE_Y=TABLE_SIZE_Y)
        print(help_text)
