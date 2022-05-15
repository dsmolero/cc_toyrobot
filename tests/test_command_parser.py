import pytest
from dataclasses import dataclass
from core.command_parser import parse_cmd, parse_place_params


class TestParseCmd:

    @dataclass
    class Parameter:
        cmd: str
        expected_output: tuple

    @dataclass
    class Fixture:
        actual_output: tuple
        expected_output: tuple

    @pytest.fixture(
        ids=[
            'test command with correct parameters',
            'test command with two parameters',
            'test command with one parameter',
            'test command with no parameters',
            'test command with too many parameters',
        ],
        params=[
            Parameter(cmd='place 3,2,north', expected_output=('place', ['3', '2', 'north'])),
            Parameter(cmd='place 3,2', expected_output=('place', ['3', '2'])),
            Parameter(cmd='place 3', expected_output=('place', ['3'])),
            Parameter(cmd='move', expected_output=('move', [])),
            Parameter(cmd='place 3,2,north,extra,etc', expected_output=('place', ['3', '2', 'north', 'extra', 'etc'])),
        ]
    )
    def setup(self, request):
        param:TestParseCmd.Parameter = request.param
        actual_output = parse_cmd(param.cmd)
        return TestParseCmd.Fixture(
            actual_output=actual_output,
            expected_output=param.expected_output
        )

    def test_parse_cmd(self, setup):
        assert setup.actual_output == setup.expected_output


class TestParsePlaceParams:

    @dataclass
    class Parameter:
        args: list
        expected_output: dict

    @dataclass
    class Fixture:
        actual_output: dict
        expected_output: dict

    @pytest.fixture(
        ids=[
            'test valid args for place command',
            'test args with four items',
            'test args with two items',
            'test args with one item',
            'test args with no items',
        ],
        params=[
            Parameter(args=['0', '1', 'north'], expected_output={'x': '0', 'y': '1', 'f': 'north'}),
            Parameter(args=['1', '2', 'north', 'extra'], expected_output={'x': '1', 'y': '2', 'f': 'north'}),
            Parameter(args=['2', '3'], expected_output={'x': '2', 'y': '3'}),
            Parameter(args=['3'], expected_output={'x': '3'}),
            Parameter(args=[], expected_output={}),
        ]
    )
    def setup(self, request):
        param:TestParsePlaceParams.Parameter = request.param
        actual_output = parse_place_params(param.args)
        return TestParsePlaceParams.Fixture(
            actual_output=actual_output,
            expected_output=param.expected_output
        )

    def test_parse_place_params(self, setup:Fixture):
        assert setup.actual_output == setup.expected_output
