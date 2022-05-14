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
            func = self.import_module_and_get_func(validator)
            if not func(self, command, *args, **kwargs):
                return False
        full_module_name = ToyRobot.command_map[command]
        func = self.import_module_and_get_func(full_module_name)
        return func(self, *args, **kwargs)

    def import_module_and_get_func(self, full_module_name):
        names = full_module_name.split('.')
        module = importlib.import_module('.'.join(names[:-1]))
        return getattr(module, names[-1])
