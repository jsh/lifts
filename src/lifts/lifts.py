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


def main() -> None:
    print(f"n = {sequence_length()}")
    print(random_floats(sequence_length()))


if __name__ == "__main__":
    main()
