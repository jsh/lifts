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


def print_float_list(float_list: list[float]) -> None:
    """
    Print a list of floats with 2-decimal-place accuracy.

    Args:
        float_list (list[float]): The list of floats to print
    """
    formatted_floats = [f"{num:.2f}" for num in float_list]
    print(formatted_floats)


def main() -> None:
    print(f"n = {sequence_length()}")
    print_float_list(random_floats(sequence_length()))


if __name__ == "__main__":
    main()
