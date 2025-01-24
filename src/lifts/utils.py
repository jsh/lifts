import random
import sys
from collections import Counter
from itertools import permutations
from math import factorial

from pydantic import PositiveInt
from sympy.functions.combinatorial.numbers import harmonic

from .lifts import Lifts

DEFAULT_NUMBER_OF_ELEMENTS = 3
USAGE = "usage: sys.argv[0] [sequence_length]"


def number_of_elements() -> PositiveInt:
    """
    Parse sys.argv and return a PositiveInt.

    If the first argument is a PositiveInt, return it.
    If there are no arguments, return 10.
    Otherwise, print a usage message to stderr and exit.
    """
    if len(sys.argv) > 2:
        n = -1
    elif len(sys.argv) == 1:
        n = DEFAULT_NUMBER_OF_ELEMENTS
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


def main() -> None:
    """
    Main function to execute the lift counting process.

    This function retrieves the sequence length, counts the number of lifts for each
    possible length in all permutations of integers from 1 to n, and compares these
    counts to the Stirling numbers of the first kind. Discrepancies are printed out.

    Returns:
        None
    """

    n = number_of_elements()
    number_of_lifts = Counter()
    lift_lengths = Counter()
    fixed_points = 0
    # lift_stats(n)
    for sequence in permutations(range(n)):
        lifts = Lifts(sequence)
        lifts.print_lifts()
        print("---")
        number_of_lifts[lifts.lift_count] += 1
        lift_lengths += lifts.lift_lengths
        fixed_points += lifts.fixed_points

    lift_lengths = Counter(dict(sorted(lift_lengths.items())))
    number_of_lifts = Counter(dict(sorted(number_of_lifts.items())))
    print(f"{lift_lengths=}"), print(f"{number_of_lifts=}")

    total_lift_length = sum(key * value for key, value in lift_lengths.items())
    total_lifts = sum(key * value for key, value in number_of_lifts.items())

    n_fact = factorial(n)
    n_harmonic = harmonic(n)
    print(f"{total_lift_length=}, {n_fact * n}")
    print(f" {total_lifts=}, {n_fact * n_harmonic}")

    #    lifts = decompose_into_lifts(sequence)
    #    print_lifts(lifts)
    # lift_counts = count_lifts(n)
    # for k, count in lift_counts.items():
    #     if count != stirling(n, k, kind=1):
    #         print(f"{k}:{count} is not {stirling(n, k, kind=1)}", sys.stderr)
    #         sys.exit()


if __name__ == "__main__":
    main()
