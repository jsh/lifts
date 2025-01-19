import pytest

# from unittest.mock import patch
from lifts.lifts import color, print_lift


@pytest.mark.parametrize(
    "float_list, expected_output",
    [
        ([1.23], f"{color(1.23)}"),
        ([1.23, 2.34, 3.45], f"{color(1.23)} 2.34 3.45"),
        ([-1.23], f"{color(-1.23)}"),
    ],
)
def test_print_lift(capsys, float_list, expected_output):
    print_lift(float_list)
    captured = capsys.readouterr()
    assert captured.out == expected_output + "\n"
