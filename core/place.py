from core.toyrobot import ToyRobot
from settings import Face


def place(bot:ToyRobot, x:int, y:int, f:str):
    bot.set_x(x)
    bot.set_y(y)
    bot.set_f(f)
