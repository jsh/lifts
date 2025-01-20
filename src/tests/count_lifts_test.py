from collections import Counter

import pytest
from sympy.functions.combinatorial.numbers import stirling

from lifts.lifts import count_lifts


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, Counter({1: 1})),
        (3, Counter({1: 2, 2: 3, 3: 1})),
        (5, Counter({1: 24, 2: 50, 3: 35, 4: 10, 5: 1})),
    ],
)
def test_count_lifts(n, expected):
    assert count_lifts(n) == expected


n_values = list(range(1, 11))


@pytest.mark.parametrize("n", n_values)
def test_count_lifts_matches_stirling(n):
    for k, count in count_lifts(n).items():
        assert count == stirling(n, k, kind=1)
