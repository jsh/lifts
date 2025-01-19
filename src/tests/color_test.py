from lifts.lifts import color


def test_simple_string():
    input_string = "Hello World"
    expected_output = "\033[92mHello World\033[0m"
    assert color(input_string) == expected_output


def test_empty_string():
    input_string = ""
    expected_output = "\033[92m\033[0m"
    assert color(input_string) == expected_output


def test_special_characters():
    input_string = "Hello @#$ World"
    expected_output = "\033[92mHello @#$ World\033[0m"
    assert color(input_string) == expected_output


def test_ansi_escape_codes():
    input_string = "\033[31mRed\033[0m"
    expected_output = "\033[92m\033[31mRed\033[0m\033[0m"
    assert color(input_string) == expected_output
