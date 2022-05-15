from core.toyrobot import ToyRobot


def report(bot:ToyRobot):
    return f'{bot.x},{bot.y},{bot.f.value.upper()}'
