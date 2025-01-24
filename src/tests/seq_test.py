from lifts.utils import seq


def test_length():
    n = 10
    assert len(seq(n)) == n


def test_contents():
    n = 10
    assert set(seq(n)) == set(range(n))


def test_shuffled():
    n = 10
    assert seq(n) != list(range(n))
