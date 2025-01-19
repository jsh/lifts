from lifts.lifts import decompose_into_lifts


def test_empty_sequence():
    assert decompose_into_lifts([]) == []


def test_single_element_sequence():
    assert decompose_into_lifts([1]) == [[1]]


def test_multiple_element_sequence_single_lift():
    assert decompose_into_lifts([1, 2, 3]) == [[1, 2, 3]]


def test_multiple_element_sequence_multiple_lifts():
    assert decompose_into_lifts([1, 2, 3, 0, 4, 5]) == [[1, 2, 3], [0, 4, 5]]


def test_sequence_with_negative_numbers():
    assert decompose_into_lifts([-1, 0, 1, -2, 2, 3]) == [[-1, 0, 1], [-2, 2, 3]]
