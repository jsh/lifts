import random
import sys

from pydantic import PositiveInt

USAGE = "usage: sys.argv[0] [sequence_length]"


def sequence_length():
    """
    Return the sequence length specified as an argument, or 10 if no argument is given.
    If the argument is not a positive integer, print the usage message and exit.

    Returns:
        int: The sequence length
    """
    if len(sys.argv) > 2:
        n = -1
    elif len(sys.argv) == 1:
        n = 10
    else:
        try:
            n = int(sys.argv[1])
            if n <= 0:
                n = -1
        except ValueError:
            n = -1

    if n == -1:  # error: non-int, negative int, or too many args
        print(USAGE, file=sys.stderr)
        sys.exit()

    return n


def random_floats(n: PositiveInt) -> list[float]:
    """
    Return a list of n random floats between 0 and 1

    Args:
        n (int): The number of random floats to generate

    Returns:
        List[float]: The list of random floats
    """
    return [random.random() for _ in range(n)]


def print_float_list(float_list: list[float]) -> None:
    """
    Print a list of floats with 2-decimal-place accuracy.

    Args:
        float_list (list[float]): The list of floats to print
    """
    print([f"{num:.2f}" for num in float_list])


def is_lift(float_list: list[float]) -> bool:
    """
    Return True iff the first element of the list is its smallest

    Args:
        float_list (list[float]): The list to check

    Returns:
        bool: True iff the first element is the smallest
        Empty lists are not lifts.
    """
    return float_list and float_list[0] == min(float_list)


def color(string: str) -> str:
    """
    Return a string with ANSI color codes wrapped around it

    Args:
        string (str): The string to convert

    Returns:
        str: The string wrapped in ANSI codes
    """
    color = "\033[92m"  # green
    end = "\033[0m"
    return f"{color}{string}{end}"


def print_lift(float_list: list[float]) -> None:
    """
    Print a lift of floats with 2-decimal-place accuracy.
    Elements are separated by a space.
    First lift element is in green.

    Args:
        float_list (list[float]): The list of floats to print
    """
    formatted_floats = [f"{num:.2f}" for num in float_list]
    formatted_floats[0] = color(formatted_floats[0])
    print(" ".join(map(str, formatted_floats)))


def decompose_into_lifts(float_list: list[float]) -> list[list[float]]:
    """
    Decompose a list into a list of lists, where each sublist is a run of consecutive increasing numbers,
    and the first element of each sublist is the smallest element in the sublist.

    Args:
        float_list (list[float]): The list to decompose

    Returns:
        list[list[float]]: A list of lists, where each sublist is a run
    """
    if not float_list:
        return []

    runs = []
    current_run = [float_list[0]]
    current_run_min = float_list[0]

    for i in range(1, len(float_list)):
        if float_list[i] > current_run_min:
            current_run.append(float_list[i])
            current_run_min = min(current_run_min, float_list[i])
        else:
            runs.append(current_run)
            current_run = [float_list[i]]
            current_run_min = float_list[i]

    runs.append(current_run)
    return runs


def print_lifts(lifts: list[list[float]]) -> None:
    for lift in lifts:
        print_lift(lift)


def main() -> None:
    # print(f"n = {sequence_length()}")
    list = random_floats(sequence_length())
    print_float_list(list)
    lifts = decompose_into_lifts(list)
    print_lifts(lifts)


if __name__ == "__main__":
    main()
