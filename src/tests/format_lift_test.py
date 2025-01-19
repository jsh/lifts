import pytest

from lifts.lifts import color, format_lift


def test_single_element_list():
    lift = [1]
    expected_output = f"{color(1)}"
    assert format_lift(lift) == expected_output


def test_multi_element_list():
    lift = [1, 2, 3]
    expected_output = f"{color(1)} 2 3"
    assert format_lift(lift) == expected_output


def test_empty_list():
    lift = []
    with pytest.raises(IndexError):
        format_lift(lift)
