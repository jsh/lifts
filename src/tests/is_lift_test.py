from lifts.lifts import is_lift


def test_empty_list():
    assert is_lift([]) is False


def test_single_element():
    assert is_lift([1]) is True


def test_first_element_smallest():
    assert is_lift([1, 2, 3]) is True


def test_first_element_not_smallest():
    assert is_lift([2, 1, 3]) is False
