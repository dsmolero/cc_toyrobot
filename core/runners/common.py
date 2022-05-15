from core.toyrobot import ToyRobot
from core.command_parser import parse_cmd, parse_place_params
from settings import  Command, HELP_COMMANDS, HELP_FILE, TABLE_SIZE_X, TABLE_SIZE_Y


class Runner:

    def __init__(self, cmd_generator):
        self.cmd_generator = cmd_generator

    def run(self):
        bot = ToyRobot()
        for cmd in self.cmd_generator():
            command, params = parse_cmd(cmd)
            if not command:
                continue
            elif cmd in ['quit', 'exit', 'q', 'x']:
                break
            elif command in HELP_COMMANDS:
                self._show_help(HELP_FILE)
            elif command == Command.PLACE.value:
                kwargs = parse_place_params(*params)
                bot.dispatch(command, **kwargs)
            else:
                bot.dispatch(command)

    def _show_help(self, help_file):
        with open(help_file, 'r') as help_file:
            help_text = help_file.read().format(TABLE_SIZE_X=TABLE_SIZE_X, TABLE_SIZE_Y=TABLE_SIZE_Y)
            print(help_text)
