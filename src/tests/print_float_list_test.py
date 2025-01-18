from lifts.lifts import print_float_list


def test_positive_floats(capsys):
    float_list = [1.2345, 2.3456, 3.4567]
    print_float_list(float_list)
    captured = capsys.readouterr()
    assert captured.out == "['1.23', '2.35', '3.46']\n"


def test_negative_floats(capsys):
    float_list = [-1.2345, -2.3456, -3.4567]
    print_float_list(float_list)
    captured = capsys.readouterr()
    assert captured.out == "['-1.23', '-2.35', '-3.46']\n"


def test_mixed_floats(capsys):
    float_list = [1.2345, -2.3456, 3.4567]
    print_float_list(float_list)
    captured = capsys.readouterr()
    assert captured.out == "['1.23', '-2.35', '3.46']\n"


def test_zero(capsys):
    float_list = [0.0, 0.0, 0.0]
    print_float_list(float_list)
    captured = capsys.readouterr()
    assert captured.out == "['0.00', '0.00', '0.00']\n"


def test_empty_list(capsys):
    float_list = []
    print_float_list(float_list)
    captured = capsys.readouterr()
    assert captured.out == "[]\n"
