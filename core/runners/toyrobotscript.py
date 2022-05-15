import os
from core.runners.common import Runner


g_script_file: str = ''


def toyrobotscript_runner(script_file:str):
    global g_script_file
    g_script_file = script_file
    runner = Runner(cmd_generator)
    runner.run()


def cmd_generator():
    global g_script_file
    with open(g_script_file, 'r') as f:
        cmd = f.readline()
        while cmd:
            print(cmd, end='')
            yield cmd
            cmd = f.readline()
    return 'exit'
