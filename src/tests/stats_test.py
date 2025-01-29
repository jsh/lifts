from collections import Counter
from itertools import permutations
from math import exp, factorial

from sympy.functions.combinatorial.numbers import stirling

from streaks.streaks import Streaks


def test_stirling():
    """
    Test the relationship between streak counts and Stirling numbers of the first kind.

    This test calculates the streak counts for all permutations of integers from 0 to n-1
    and asserts that the count for each number of streaks matches the corresponding Stirling
    number of the first kind.

    The Stirling number of the first kind, s(n, k), counts the number of permutations
    of n elements with exactly k permutation cycles (streaks in this context).
    """

    n = 5
    streak_counts = Counter()
    for sequence in permutations(range(n)):
        streaks = Streaks(sequence)
        number_of_streaks = streaks.streak_count
        streak_counts[number_of_streaks] += 1
    for k, count in streak_counts.items():
        assert count == stirling(n, k, kind=1)


def test_derangement_estimate():
    """
    Test the goodness of a Poisson for estimating
    the number of permutations with no streaks of length 1.

    The total number of streaks of length 1, over all N! permutations,
    should be N!, so the expected number per permutation is 1.
    The Poisson distribution says that P(0), the probability of no length-1 streaks,
    should be e^(-1), so the expected number over all permutations should be N!/e.

    We'll call a permutation with no length-1 streaks a "derangement,"
    because the math is the same as for permutation cycles.

    This test compares round(N!/e) to the observed number.
    """
    for n in range(1, 10):
        observed_derangements = 0
        for sequence in permutations(range(n)):
            streaks = Streaks(sequence)
            if streaks.fixed_points_count == 0:  # no fixed points
                observed_derangements += 1
        # derangements is now number of derangements over all permutations, length n
        expected_derangements = factorial(n) * exp(-1)
        assert observed_derangements == round(expected_derangements)
