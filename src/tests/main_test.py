"""
def test_main_does_not_return_any_value():
    assert main() is None


def test_main_prints_to_stdout(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() != ""
"""

import pytest

from lifts.lifts import main


@pytest.fixture
def mock_sequence_length(monkeypatch):
    with monkeypatch.context() as mp:
        mp.setattr("lifts.lifts.sequence_length", lambda: 10)
        yield


def test_main_prints_correct_output(mock_sequence_length, capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "n = 10"
