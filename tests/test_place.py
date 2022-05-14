import pytest
from settings import Command, Face, TABLE_SIZE_X, TABLE_SIZE_Y
from unittest.mock import Mock, patch
from dataclasses import dataclass
from core import toyrobot


class TestPlace:

    @dataclass
    class Parameter:
        x: object
        y: object
        f: str
        is_valid: bool

    @dataclass
    class Fixture:
        x: object
        y: object
        f: str
        bot: toyrobot.ToyRobot
        mock_log: Mock
        is_valid: bool

    @pytest.fixture(
        ids=[
            'test x and y are integers',
            'test x should be an integer',
            'test y should be an integer',
            'test x should not be negative',
            'test y should not be negative',
            'test x should not exceed TABLE_SIZE_X',
            'test y should not exceed TABLE_SIZE_Y',
            'test f should only be either NORTH, EAST, WEST or SOUTH',
        ],
        params=[
            Parameter(x=0, y=0, f=Face.NORTH, is_valid=True),
            Parameter(x='3', y=2, f=Face.NORTH, is_valid=False),
            Parameter(x=2, y='3', f=Face.NORTH, is_valid=False),
            Parameter(x=-1, y=3, f=Face.NORTH, is_valid=False),
            Parameter(x=3, y=-1, f=Face.NORTH, is_valid=False),
            Parameter(x=TABLE_SIZE_X + 1, y=1, f=Face.NORTH, is_valid=False),
            Parameter(x=1, y=TABLE_SIZE_Y + 1, f=Face.NORTH, is_valid=False),
            Parameter(x=4, y=4, f='CENTER', is_valid=False),
        ]
    )
    @patch('core.validators.place.log')
    def setup(self, mock_log, request):
        bot: toyrobot.ToyRobot = toyrobot.ToyRobot()
        kwargs = {'x': request.param.x, 'y': request.param.y, 'f': request.param.f}
        bot.dispatch(Command.PLACE, **kwargs)
        return TestPlace.Fixture(
            **kwargs,
            bot=bot,
            mock_log=mock_log,
            is_valid=request.param.is_valid
        )

    def test_place(self, setup):
        has_errors = setup.mock_log.error.call_count > 0
        if setup.is_valid:
            assert setup.bot.x == setup.x
            assert setup.bot.y == setup.y
            assert setup.bot.f == setup.f
            assert not has_errors
        else:
            assert has_errors
