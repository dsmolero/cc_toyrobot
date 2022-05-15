from core.toyrobot import ToyRobot


def place(bot:ToyRobot, x:int, y:int, f:str):
    bot.set_x(x)
    bot.set_y(y)
    bot.set_f(f)
