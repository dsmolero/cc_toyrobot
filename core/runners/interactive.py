from logging import getLogger
from core.runners.common import Runner


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
