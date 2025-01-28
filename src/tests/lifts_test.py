from collections import Counter

import pytest

from lifts.lifts import Lifts

# test __init__()


def test_empty_list():
    instance = Lifts([])
    assert instance.lifts == []


def test_single_element_list():
    instance = Lifts([1])
    assert instance.lifts == [[1]]


def test_ascending_list():
    instance = Lifts([1, 2, 3, 4, 5])
    assert instance.lifts == [[1, 2, 3, 4, 5]]
    instance2 = Lifts([1, 2, 3, 4, 5], reverse=True)
    assert instance2.lifts == [[1], [2], [3], [4], [5]]


def test_descending_list():
    instance = Lifts([5, 4, 3, 2, 1])
    assert instance.lifts == [[5], [4], [3], [2], [1]]
    instance = Lifts([5, 4, 3, 2, 1], reverse=True)
    assert instance.lifts == [[5, 4, 3, 2, 1]]


def test_random_list():
    instance = Lifts([3, 1, 4, 2, 5])
    assert instance.lifts == [[3], [1, 4, 2, 5]]
    instance = Lifts([3, 1, 4, 2, 5], reverse=True)
    assert instance.lifts == [[3, 1], [4, 2], [5]]


# test lift_lengths property


def test_empty_lift_list():
    instance = Lifts([])
    assert instance.lift_lengths == Counter()


def test_singleton_lift_list():
    instance = Lifts([1])
    assert instance.lift_lengths == Counter({1: 1})


def test_multiple_lifts():
    instance = Lifts([4, 5, 6, 3, 1, 2])
    assert instance.lift_lengths == Counter({1: 1, 3: 1, 2: 1})


def test_multiple_lifts_same_length():
    instance = Lifts([5, 6, 3, 4, 1, 2])
    assert instance.lift_lengths == Counter({2: 3})


# test lift_count


def test_lift_count_empty():
    instance = Lifts([])
    assert instance.lift_count == 0


def test_lift_count_single():
    instance = Lifts([1])
    assert instance.lift_count == 1


def test_lift_count_multiple():
    instance = Lifts([1, 2, 3, 4, 5])
    assert (
        instance.lift_count == 1
    )  # Note: This is because decompose_into_lifts will create a single lift for this sequence


def test_lift_count_multiple_lifts():
    instance = Lifts([5, 4, 3, 2, 1])
    assert (
        instance.lift_count == 5
    )  # Note: This is because decompose_into_lifts will create multiple lifts for this sequence


# test decompose_into_lifts()


@pytest.fixture
def lifts():
    return Lifts([])


def test_empty_sequence(lifts):
    assert lifts.decompose_into_lifts([]) == []


def test_single_element_sequence(lifts):
    assert lifts.decompose_into_lifts([1]) == [[1]]


def test_increasing_sequence(lifts):
    assert lifts.decompose_into_lifts([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5]]


def test_decreasing_sequence(lifts):
    assert lifts.decompose_into_lifts([5, 4, 3, 2, 1]) == [[5], [4], [3], [2], [1]]


def test_mixed_sequence(lifts):
    assert lifts.decompose_into_lifts([4, 3, 9, 7, 5, 1, 2]) == [
        [4],
        [3, 9, 7, 5],
        [1, 2],
    ]


# test print_lifts()


def test_print_single_lift(capsys):
    lifts = Lifts([1])
    lifts.print_lifts()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m"


def test_print_multiple_elements_lift(capsys):
    lifts = Lifts([1, 2, 3])
    lifts.print_lifts()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m 2 3"


def test_print_multiple_lifts(capsys):
    lifts = Lifts([1, 2, 3, 4, 5, 6])
    lifts.lifts = [[1, 2, 3], [4, 5, 6]]
    lifts.print_lifts()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m 2 3\n\x1b[92m4\x1b[0m 5 6"


def test_print_empty_lifts(capsys):
    lifts = Lifts([])
    lifts.print_lifts()
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


# test format_lift()


def test_single_element_lift(lifts):
    lift = [1]
    expected_output = "\x1b[92m1\x1b[0m"
    assert lifts.format_lift(lift) == expected_output


def test_multiple_element_lift(lifts):
    lift = [1, 2, 3]
    expected_output = "\x1b[92m1\x1b[0m 2 3"
    assert lifts.format_lift(lift) == expected_output


def test_first_element_colored_green(lifts):
    lift = [1, 2, 3]
    formatted_lift = lifts.format_lift(lift)
    assert "\x1b[92m" in formatted_lift  # check for green color code


def test_empty_lift(lifts):
    lift = []
    expected_output = ""
    assert lifts.format_lift(lift) == expected_output


# test color()


def test_single_character_string(lifts):
    assert lifts.color("a") == "\033[92ma\033[0m"


def test_multi_character_string(lifts):
    assert lifts.color("hello") == "\033[92mhello\033[0m"


def test_empty_string(lifts):
    assert lifts.color("") == "\033[92m\033[0m"


def test_string_with_special_characters(lifts):
    assert lifts.color("!@#$") == "\033[92m!@#$\033[0m"
