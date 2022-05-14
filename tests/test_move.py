import pytest
from settings import Command, Face
from unittest.mock import Mock, patch
from dataclasses import dataclass
from core import toyrobot


class TestMove:

    @dataclass
    class Parameter:
        x: int
        y: int
        f: str
        new_x: int
        new_y: int
        can_move: bool

    @dataclass
    class Fixture:
        bot: toyrobot.ToyRobot
        new_x: int
        new_y: int
        can_move: bool
        mock_log: Mock

    @pytest.fixture(
        ids=[
            'test valid move to the north',
            'test valid move to the east',
            'test valid move to the south',
            'test valid move to the west',
            'test invalid move to the north',
            'test invalid move to the east',
            'test invalid move to the south',
            'test invalid move to the west',
        ],
        params=[
            Parameter(x=1, y=3, f=Face.NORTH, new_x=1, new_y=4, can_move=True),
            Parameter(x=3, y=1, f=Face.EAST, new_x=4, new_y=1, can_move=True),
            Parameter(x=3, y=1, f=Face.SOUTH, new_x=3, new_y=0, can_move=True),
            Parameter(x=1, y=3, f=Face.WEST, new_x=0, new_y=3, can_move=True),
            Parameter(x=1, y=4, f=Face.NORTH, new_x=1, new_y=4, can_move=False),
            Parameter(x=4, y=1, f=Face.EAST, new_x=4, new_y=1, can_move=False),
            Parameter(x=3, y=0, f=Face.SOUTH, new_x=3, new_y=0, can_move=False),
            Parameter(x=0, y=3, f=Face.WEST, new_x=0, new_y=3, can_move=False),
        ]
    )
    @patch('core.validators.move.log')
    def setup(self, mock_log: Mock, request):
        param = request.param
        bot = toyrobot.ToyRobot()
        bot.dispatch(Command.PLACE, x=param.x, y=param.y, f=param.f)
        bot.dispatch(Command.MOVE)
        return TestMove.Fixture(
            bot=bot,
            new_x=param.new_x,
            new_y=param.new_y,
            can_move=param.can_move,
            mock_log=mock_log
        )

    def test_move(self, setup: Fixture):
        has_errors = setup.mock_log.error.call_count > 0
        if setup.can_move:
            assert setup.bot.x == setup.new_x
            assert setup.bot.y == setup.new_y
            assert not has_errors
        else:
            assert has_errors
