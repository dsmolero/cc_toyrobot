import pytest
from settings import Command, Face
from unittest.mock import Mock, patch
from dataclasses import dataclass
from core.toyrobot import ToyRobot


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
        bot: ToyRobot
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
            'test move to the north will go out of bounds',
            'test move to the east will go out of bounds',
            'test move to the south will go out of bounds',
            'test move to the west will go out of bounds',
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
        bot = ToyRobot()
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


class TestMoveMiscCases:

    @patch('core.validators.report.log')
    def test_move_before_place(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.MOVE)
        mock_log.error.assert_called_once()

    @patch('core.validators.common.log')
    def test_move_with_unexpected_params(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=3, y=3, f=Face.NORTH)
        bot.dispatch(Command.MOVE, 'some_param', unexpected_param='unexpected param')
        mock_log.error.assert_called_once()
