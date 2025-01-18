import sys

import pytest

from lifts.lifts import USAGE, sequence_length


@pytest.fixture
def mock_sys_argv(monkeypatch):
    def mock_argv(argv):
        monkeypatch.setattr(sys, "argv", argv)

    return mock_argv


def test_default_sequence_length(mock_sys_argv):
    mock_sys_argv(["script_name"])
    assert sequence_length() == 10


def test_sequence_length_with_valid_integer(mock_sys_argv):
    mock_sys_argv(["script_name", "5"])
    assert sequence_length() == 5


def test_sequence_length_with_negative_integer(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "-5"])
    with pytest.raises(SystemExit):
        sequence_length()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE


def test_sequence_length_with_invalid_argument(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "abc"])
    with pytest.raises(SystemExit):
        sequence_length()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE


def test_sequence_length_with_too_many_arguments(mock_sys_argv, capsys):
    mock_sys_argv(["script_name", "5", "10"])
    with pytest.raises(SystemExit):
        sequence_length()
    captured = capsys.readouterr()
    assert captured.err.strip() == USAGE
