import pytest

from lifts.lifts import color, print_lifts


@pytest.mark.parametrize(
    "lifts, expected_output",
    [
        ([], ""),
        ([[1.01, 2.02, 3.03]], f"{color(1.01)} 2.02 3.03\n"),
        (
            [[1.01, 2.02, 3.03], [4.04, 5.05, 6.06]],
            f"{color(1.01)} 2.02 3.03\n{color(4.04)} 5.05 6.06\n",
        ),
    ],
)
def test_print_lifts(lifts, expected_output, capsys):
    print_lifts(lifts)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    print_lifts([])
    captured = capsys.readouterr()
    assert captured.out == ""


def test_print_lifts_single_lift(capsys):
    lifts = [[1.01, 2.02, 3.03]]
    expected_output = f"{color(1.01)} 2.02 3.03\n"
    print_lifts(lifts)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_lifts_multiple_lifts(capsys):
    lifts = [[1.01, 2.02, 3.03], [4.04, 5.05, 6.06]]
    expected_output = f"{color(1.01)} 2.02 3.03\n{color(4.04)} 5.05 6.06\n"
    print_lifts(lifts)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_lifts_lifts_with_different_lengths(capsys):
    lifts = [[1.01, 2.02], [3.03, 4.04, 5.05]]
    expected_output = f"{color(1.01)} 2.02\n{color(3.03)} 4.04 5.05\n"
    print_lifts(lifts)
    captured = capsys.readouterr()
    assert captured.out == expected_output
