import pprint
import sys
from collections import Counter
from itertools import permutations
from math import factorial

from pydantic import PositiveInt
from sympy.functions.combinatorial.numbers import harmonic

from .streaks import Streaks

DEFAULT_NUMBER_OF_ELEMENTS = 3
USAGE = "usage: sys.argv[0] [sequence_length]"


def number_of_elements() -> PositiveInt:
    """
    Parse sys.argv and return a PositiveInt.

    If the only argument is a PositiveInt, return it.
    If there are no arguments, return DEFAULT_NUMBER_OF_ELEMENTS.
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


def main() -> None:
    """
    Main function to execute the streak counting process.

    This function retrieves the sequence length, counts the number of streaks for each
    possible length in all permutations of integers from 1 to n, and compares these
    counts to the Stirling numbers of the first kind. Discrepancies are printed out.

    Returns:
        None
    """

    n = number_of_elements()
    number_of_streaks = Counter()
    streak_lengths = Counter()
    fixed_points = 0
    # streak_stats(n)
    for sequence in permutations(range(n)):
        streaks = Streaks(sequence)
        streaks.print_streaks()
        print("---")
        number_of_streaks[streaks.streak_count] += 1
        streak_lengths += streaks.streak_lengths
        fixed_points += streaks.fixed_points

    pprint.pprint(f"{streak_lengths=}, {fixed_points=}")
    pprint.pprint(f"{dict(sorted(number_of_streaks.items()))=}")

    total_streak_length = sum(key * value for key, value in streak_lengths.items())
    total_streaks = sum(key * value for key, value in number_of_streaks.items())

    n_fact = factorial(n)
    n_harmonic = harmonic(n)
    print(f"{total_streak_length=}, {n_fact * n}")
    print(f" {total_streaks=}, {n_fact * n_harmonic}")

    # for k, count in streak_counts.items():
    #     if count != stirling(n, k, kind=1):
    #         print(f"{k}:{count} is not {stirling(n, k, kind=1)}", sys.stderr)
    #         sys.exit()


if __name__ == "__main__":
    main()
