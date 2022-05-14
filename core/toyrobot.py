import importlib


class ToyRobot:
    command_map = {}
    validators = []
    _x: int
    _y: int
    _f: str

    def __init__(self):
        self._x : int = -1
        self._y : int = -1
        self._f : str = ''

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def f(self):
        return self._f

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_f(self, f):
        self._f = f

    def dispatch(self, command, *args, **kwargs):
        for validator in ToyRobot.validators:
            names = validator.split('.')
            module = importlib.import_module('.'.join(names[:-1]))
            func = getattr(module, names[-1])
            if not func(self, command, *args, **kwargs):
                return False
        func = ToyRobot.command_map[command]
        return func(self, *args, **kwargs)
