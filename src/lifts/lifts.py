import random
import sys
from collections import Counter
from itertools import permutations
from typing import Iterator, List, Tuple

from pydantic import PositiveInt

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


def permutation_lifts(lifts: List[int]) -> Iterator[Tuple[List[int], ...]]:
    """
    Generate each permutation of a list broken into lifts.

    Args:
        lifts (List[int]): The list of elements to generate permutations from

    Yields:
        Tuple[List[int], ...]: A permutation of the input list broken into lifts
    """
    for p in permutations(lifts):
        yield tuple(decompose_into_lifts(p))


def print_lifts(lifts: list[list[int]]) -> None:
    """
    Print each lift in a list of lifts, with the first element of each lift colored.

    Args:
        lifts (list[list[int]]): The list of lifts to print.
    """
    for lift in lifts:
        print(format_lift(lift))


def lift_stats(n: int) -> Counter:
    """
    Count the number of lifts of length k in all permutations of the set of positive integers {1, 2, ..., n}

    Args:
        n (PositiveInt): The upper limit of the set of positive integers to consider

    Returns:
        Counter: A Counter mapping each possible length of lift to the number of such lifts in all permutations
    """
    lift_counts = Counter()
    lift_lengths = Counter()
    shortest_lift_counts = Counter()
    longest_lift_counts = Counter()
    total = 0
    for lift_list in permutation_lifts(seq(n)):
        # print_lifts(lift_list)
        total += 1
        lift_counts[len(lift_list)] += 1
        lift_lengths = [len(lift) for lift in lift_list]
        shortest_lift_counts[min(lift_lengths)] += 1
        longest_lift_counts[max(lift_lengths)] += 1

    assert (
        total
        == lift_counts.total()
        == shortest_lift_counts.total()
        == longest_lift_counts.total()
    )
    for counter in lift_counts, shortest_lift_counts, longest_lift_counts:
        print(f"{counter=}")
    return lift_counts


def main() -> None:
    """
    Main function to execute the lift counting process.

    This function retrieves the sequence length, counts the number of lifts for each
    possible length in all permutations of integers from 1 to n, and compares these
    counts to the Stirling numbers of the first kind. Discrepancies are printed out.

    Returns:
        None
    """

    n = sequence_length()
    lift_stats(n)
    # for sequence in permutations(range(n)):
    #    print(sequence)
    #    lifts = decompose_into_lifts(sequence)
    #    print_lifts(lifts)
    # lift_counts = count_lifts(n)
    # for k, count in lift_counts.items():
    #     if count != stirling(n, k, kind=1):
    #         print(f"{k}:{count} is not {stirling(n, k, kind=1)}", sys.stderr)
    #         sys.exit()

    # print("same!")
    # decomps = permutation_lifts(seq(n))
    # for d in decomps:
    #     # print_lifts(d)
    #     # print("---")
    #     lift_stats(d)


if __name__ == "__main__":
    main()
