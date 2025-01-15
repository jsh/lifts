import sys

from lifts.lifts import usage  # replace 'your_module' with the actual module name


def test_usage_prints_to_stderr(capsys):
    usage()
    captured = capsys.readouterr()
    assert captured.err != ""
    assert captured.out == ""


def test_usage_prints_correct_message(capsys):
    usage()
    captured = capsys.readouterr()
    expected_message = f"Usage: {sys.argv[0]} [N]\n"
    assert captured.err == expected_message
