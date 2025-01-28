import sys

import pytest

from streaks.utils import DEFAULT_NUMBER_OF_ELEMENTS, USAGE, number_of_elements


@pytest.fixture
def mock_sys_argv(monkeypatch):
    def mock_argv(argv):
        monkeypatch.setattr(sys, "argv", argv)

    return mock_argv


def test_default_sequence_length(mock_sys_argv):
    mock_sys_argv(["script_name"])
    assert number_of_elements() == DEFAULT_NUMBER_OF_ELEMENTS


def test_sequence_length_with_valid_integer(mock_sys_argv):
    mock_sys_argv(["script_name", "5"])
    assert number_of_elements() == 5


def test_sequence_length_with_negative_integer(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "-5"])
    with pytest.raises(SystemExit):
        number_of_elements()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE


def test_sequence_length_with_invalid_argument(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "abc"])
    with pytest.raises(SystemExit):
        number_of_elements()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE


def test_sequence_length_with_too_many_arguments(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "5", "10"])
    with pytest.raises(SystemExit):
        number_of_elements()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE
