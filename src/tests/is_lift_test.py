import pytest

from lifts.lifts import is_lift, random_floats


@pytest.fixture
def random_lift_list():
    list = random_floats(10)
    list[0] = min(list) - 10
    return list


def test_empty_list():
    assert not is_lift([])


def test_single_element():
    assert is_lift([random_floats(10)[0]])


def test_first_element_is_smallest(random_lift_list):
    assert is_lift(random_lift_list)


def test_first_element_is_not_smallest(random_lift_list):
    assert not is_lift(random_lift_list[1:] + [random_lift_list[0]])
