import sys
from core.runners.interactive import interactive_runner
from core.runners.toyrobotscript import script_runner
from settings import USAGE_FILE, HELP_PARAMS


def _show_usage():
    with open(USAGE_FILE, 'r') as f:
        print(f.read())


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 2:
        _show_usage()
    elif len(args) == 2:
        cmd_or_filename = args[1]
        if cmd_or_filename.lower() in HELP_PARAMS:
            _show_usage()
        else:
            script_runner(cmd_or_filename)
    else:
        interactive_runner()
