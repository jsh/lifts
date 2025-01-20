import random
import sys
from collections import Counter
from itertools import permutations

from pydantic import PositiveInt
from sympy.functions.combinatorial.numbers import stirling

USAGE = "usage: sys.argv[0] [sequence_length]"


def sequence_length() -> PositiveInt:
    """
    Parse sys.argv and return a PositiveInt.

    If the first argument is a PositiveInt, return it.
    If there are no arguments, return 10.
    Otherwise, print a usage message to stderr and exit.
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


def seq(n: PositiveInt) -> list[int]:
    """
    Generate a shuffled sequence of integers from 0 to n-1.

    Args:
        n (PositiveInt): The length of the sequence to generate.

    Returns:
        list[int]: A list containing a random permutation of integers from 0 to n-1.
    """
    s = list(range(n))
    random.shuffle(s)
    return s


def is_lift(seq: list[float]) -> bool:
    """
    Return True iff the first element of the list is its smallest

    Args:
        sequence (list[sequence]): The list to check

    Returns:
        bool: True iff the first element is the smallest
        Empty lists are not lifts.
    """
    return seq != [] and seq[0] == min(seq)


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


def format_lift(lift: list[int]) -> None:
    """
    Format a lift.
    Elements are separated by a space.
    First lift element is in green.

    Args:
        lift (list[int]): The list of ints to print
    """
    lift[0] = color(lift[0])
    return " ".join(map(str, lift))


def decompose_into_lifts(seq: list[int]) -> list[list[int]]:
    """
    Decompose a sequence into its component lifts.

    A lift is a sequence of numbers such that the first number is the smallest.
    The output is a list of such lifts.

    Args:
        seq (list[int]): The sequence to decompose into lifts

    Returns:
        list[list[int]]: A list of lifts
    """
    if not seq:
        return []

    lifts = []
    current_lift = [seq[0]]
    current_lift_min = current_lift[0]

    for i in range(1, len(seq)):
        next = seq[i]
        if next > current_lift_min:
            current_lift.append(next)
            current_lift_min = min(current_lift_min, next)
        else:
            lifts.append(current_lift)
            current_lift = [seq[i]]
            current_lift_min = next

    lifts.append(current_lift)
    return lifts


def print_lifts(lifts: list[list[int]]) -> None:
    for lift in lifts:
        print(format_lift(lift))


def count_lifts(n: PositiveInt) -> Counter:
    lift_counts = Counter()

    for sequence in permutations(range(n)):
        lifts = decompose_into_lifts(sequence)
        lift_counts[len(lifts)] += 1

    return lift_counts


def main() -> None:
    n = sequence_length()
    # for sequence in permutations(range(n)):
    #    print(sequence)
    #    lifts = decompose_into_lifts(sequence)
    #    print_lifts(lifts)
    lift_counts = count_lifts(n)
    for k, count in lift_counts.items():
        if count != stirling(n, k, kind=1):
            print(f"{k}:{count} is not {stirling(n, k, kind=1)}")

    print("same!")


if __name__ == "__main__":
    main()
