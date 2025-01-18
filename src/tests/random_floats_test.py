import pytest

from lifts.lifts import random_floats


def test_random_floats_returns_list_of_floats():
    n = 10
    result = random_floats(n)
    assert isinstance(result, list)
    assert all(isinstance(num, float) for num in result)


def test_random_floats_returns_list_of_length_n():
    n = 10
    result = random_floats(n)
    assert len(result) == n


def test_random_floats_returns_numbers_between_0_and_1():
    n = 10
    result = random_floats(n)
    assert all(0 <= num <= 1 for num in result)


# def test_random_floats_raises_error_for_non_positive_n():
#     with pytest.raises(ValueError):
#         random_floats(-1)


def test_random_floats_raises_error_for_non_integer_n():
    with pytest.raises(TypeError):
        random_floats(1.5)
