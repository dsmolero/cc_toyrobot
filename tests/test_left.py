import pytest
from dataclasses import dataclass
from unittest.mock import patch
from core.toyrobot import ToyRobot
from settings import Command, Face


class TestLeftDontMove:

    def test_dont_move(self):
        x = 3
        y = 2
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=x, y=y, f=Face.NORTH)
        for ii in range(4):
            bot.dispatch(Command.LEFT)
            assert bot.x == x
            assert bot.y == y


class TestLeftNewFace:

    @dataclass
    class Parameter:
        f: str
        new_f: str

    @dataclass
    class Fixture:
        bot: ToyRobot
        new_f: str

    @pytest.fixture(
        ids=[
            'test face left to the north',
            'test face left to the east',
            'test face left to the south',
            'test face left to the west',
        ],
        params=[
            Parameter(f=Face.EAST, new_f=Face.NORTH),
            Parameter(f=Face.SOUTH, new_f=Face.EAST),
            Parameter(f=Face.WEST, new_f=Face.SOUTH),
            Parameter(f=Face.NORTH, new_f=Face.WEST),
        ]
    )
    def setup(self, request):
        param = request.param
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=3, y=2, f=param.f)
        bot.dispatch(Command.LEFT)
        return TestLeftNewFace.Fixture(
            bot=bot,
            new_f=param.new_f
        )

    def test_left(self, setup:Fixture):
        assert setup.bot.f == setup.new_f


class TestLeftMiscCases:

    @patch('core.validators.report.log')
    def test_left_before_place(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.LEFT)
        mock_log.error.assert_called_once()

    @patch('core.validators.common.log')
    def test_left_with_unexpected_params(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=3, y=3, f=Face.NORTH)
        bot.dispatch(Command.LEFT, 'some_param', unexpected_param='unexpected param')
        mock_log.error.assert_called_once()
