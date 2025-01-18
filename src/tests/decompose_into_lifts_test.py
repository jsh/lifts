from lifts.lifts import decompose_into_lifts, random_floats


def test_empty_list():
    assert decompose_into_lifts([]) == []


def test_single_element_list():
    single_element_list = [random_floats(1)[0]]
    assert decompose_into_lifts(single_element_list) == [single_element_list]


def test_one_run_of_increasing_numbers():
    increasing_list = sorted(random_floats(10))
    assert decompose_into_lifts(increasing_list) == [increasing_list]


def test_multiple_runs_of_increasing_numbers():
    # Generate a list with multiple runs of increasing numbers
    list1 = sorted(random_floats(5))
    list2 = [min(list1) - 1] + sorted(
        random_floats(5)
    )  # so second sublist won't merge with first
    multiple_runs_list = list1 + list2
    assert decompose_into_lifts(multiple_runs_list) == [list1, list2]


def test_decreasing_numbers():
    decreasing_list = sorted(random_floats(10), reverse=True)
    assert decompose_into_lifts(decreasing_list) == [[num] for num in decreasing_list]
