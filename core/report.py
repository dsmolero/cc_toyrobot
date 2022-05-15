from core.toyrobot import ToyRobot


def report(bot:ToyRobot):
    try:
        f = bot.f.value
    except AttributeError:
        f = bot.f
    return f'{bot.x},{bot.y},{f.upper()}'
