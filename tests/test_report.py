from unittest.mock import patch
from core.toyrobot import ToyRobot
from settings import Command, Face


class TestReportAfterPlace:

    @patch('builtins.print')
    def test_report_after_place(self, mock_print):
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=3, y=2, f=Face.EAST.value)
        actual_output = bot.dispatch(Command.REPORT)
        expected_output = '3,2,EAST'
        assert actual_output == expected_output
        mock_print.assert_called_once_with(expected_output)


class TestReportMiscCases:

    @patch('core.validators.common.log')
    def test_report_before_place(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.REPORT)
        mock_log.error.assert_called_once()

    @patch('core.validators.common.log')
    def test_report_with_unexpected_params(self, mock_log):
        bot = ToyRobot()
        bot.dispatch(Command.PLACE, x=3, y=3, f=Face.NORTH.value)
        bot.dispatch(Command.REPORT, 'some_param', unexpected_param='unexpected param')
        mock_log.error.assert_called_once()
