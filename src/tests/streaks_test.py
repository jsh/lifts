from collections import Counter

import pytest

from streaks.streaks import Streaks

# test __init__()


def test_empty_list():
    instance = Streaks([])
    assert instance.streaks == []


def test_single_element_list():
    instance = Streaks([1])
    assert instance.streaks == [[1]]


def test_ascending_list():
    instance = Streaks([1, 2, 3, 4, 5])
    assert instance.streaks == [[1, 2, 3, 4, 5]]
    instance2 = Streaks([1, 2, 3, 4, 5], winning=False)
    assert instance2.streaks == [[1], [2], [3], [4], [5]]


def test_descending_list():
    instance = Streaks([5, 4, 3, 2, 1])
    assert instance.streaks == [[5], [4], [3], [2], [1]]
    instance = Streaks([5, 4, 3, 2, 1], winning=False)
    assert instance.streaks == [[5, 4, 3, 2, 1]]


def test_random_list():
    instance = Streaks([3, 1, 4, 2, 5])
    assert instance.streaks == [[3], [1, 4, 2, 5]]
    instance = Streaks([3, 1, 4, 2, 5], winning=False)
    assert instance.streaks == [[3, 1], [4, 2], [5]]


# test streak__lengths_counter property


def test_empty_streak_list():
    instance = Streaks([])
    assert instance.streak_lengths_counter == Counter()


def test_singleton_streak_list():
    instance = Streaks([1])
    assert instance.streak_lengths_counter == Counter({1: 1})


def test_multiple_streaks():
    instance = Streaks([4, 5, 6, 3, 1, 2])
    assert instance.streak_lengths_counter == Counter({1: 1, 3: 1, 2: 1})


def test_multiple_streaks_same_length():
    instance = Streaks([5, 6, 3, 4, 1, 2])
    assert instance.streak_lengths_counter == Counter({2: 3})


# test streak_count


def test_streak_count_empty():
    instance = Streaks([])
    assert instance.streak_count == 0


def test_streak_count_single():
    instance = Streaks([1])
    assert instance.streak_count == 1


def test_streak_count_multiple():
    instance = Streaks([1, 2, 3, 4, 5])
    assert (
        instance.streak_count == 1
    )  # Note: This is because decompose_into_streaks will create a single streak for this sequence


def test_streak_count_multiple_streaks():
    instance = Streaks([5, 4, 3, 2, 1])
    assert (
        instance.streak_count == 5
    )  # Note: This is because decompose_into_streaks will create multiple streaks for this sequence


# test decompose_into_streaks()


@pytest.fixture
def streaks():
    return Streaks([])


def test_empty_sequence(streaks):
    assert streaks.decompose_into_streaks([]) == []


def test_single_element_sequence(streaks):
    assert streaks.decompose_into_streaks([1]) == [[1]]


def test_increasing_sequence(streaks):
    assert streaks.decompose_into_streaks([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5]]


def test_decreasing_sequence(streaks):
    assert streaks.decompose_into_streaks([5, 4, 3, 2, 1]) == [[5], [4], [3], [2], [1]]


def test_mixed_sequence(streaks):
    assert streaks.decompose_into_streaks([4, 3, 9, 7, 5, 1, 2]) == [
        [4],
        [3, 9, 7, 5],
        [1, 2],
    ]


# test print_streaks()


def test_print_single_streak(capsys):
    streaks = Streaks([1])
    streaks.print_streaks()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m"


def test_print_multiple_elements_streak(capsys):
    streaks = Streaks([1, 2, 3])
    streaks.print_streaks()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m 2 3"


def test_print_multiple_streaks(capsys):
    streaks = Streaks([1, 2, 3, 4, 5, 6])
    streaks.streaks = [[1, 2, 3], [4, 5, 6]]
    streaks.print_streaks()
    captured = capsys.readouterr()
    assert captured.out.strip() == "\x1b[92m1\x1b[0m 2 3\n\x1b[92m4\x1b[0m 5 6"


def test_print_empty_streaks(capsys):
    streaks = Streaks([])
    streaks.print_streaks()
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


# test format_streak()


def test_single_element_streak(streaks):
    streak = [1]
    expected_output = "\x1b[92m1\x1b[0m"
    assert streaks.format_streak(streak) == expected_output


def test_multiple_element_streak(streaks):
    streak = [1, 2, 3]
    expected_output = "\x1b[92m1\x1b[0m 2 3"
    assert streaks.format_streak(streak) == expected_output


def test_first_element_colored_green(streaks):
    streak = [1, 2, 3]
    formatted_streak = streaks.format_streak(streak)
    assert "\x1b[92m" in formatted_streak  # check for green color code


def test_empty_streak(streaks):
    streak = []
    expected_output = ""
    assert streaks.format_streak(streak) == expected_output


# test color()


def test_single_character_string(streaks):
    assert streaks.color("a") == "\033[92ma\033[0m"


def test_multi_character_string(streaks):
    assert streaks.color("hello") == "\033[92mhello\033[0m"


def test_empty_string(streaks):
    assert streaks.color("") == "\033[92m\033[0m"


def test_string_with_special_characters(streaks):
    assert streaks.color("!@#$") == "\033[92m!@#$\033[0m"
