from collections import Counter
from typing import List

from pydantic import PositiveInt


class Lifts:
    """
    Represent a sequence of integers as a sequence of lifts.

    A lift is a sequence of numbers such that the first number is the smallest.
    The output is a list of such lifts.
    """

    def __init__(self, ints: List[int]):
        self.lifts = self.decompose_into_lifts(ints)

    @property
    def lift_lengths(self) -> Counter:
        """A Counter mapping each possible length of lift to the number of such lifts in all permutations"""
        counter = Counter(len(lift) for lift in self.lifts)
        return Counter(dict(sorted(counter.items())))

    @property
    def fixed_points(self) -> PositiveInt:
        """A Counter mapping each possible length of lift to the number of such lifts in all permutations"""
        return self.lift_lengths[1]

    @property
    def lift_count(self) -> PositiveInt:
        return len(self.lifts)

    def decompose_into_lifts(self, seq: List[int]) -> List[List[int]]:
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
            next_ = seq[i]
            if next_ > current_lift_min:
                current_lift.append(next_)
                current_lift_min = min(current_lift_min, next_)
            else:
                lifts.append(current_lift)
                current_lift = [seq[i]]
                current_lift_min = next_

        lifts.append(current_lift)
        return lifts

    def print_lifts(self) -> None:
        """
        Print each lift in the list of lifts, with the first element of each lift colored.
        """
        for lift in self.lifts:
            print(self.format_lift(lift))

    def format_lift(self, lift: list[int]) -> str:
        """
        Format a lift.
        Elements are separated by a space.
        First lift element is in green.

        Args:
            lift (list[int]): The list of ints to print
        """
        lift[0] = self.color(lift[0])
        return " ".join(map(str, lift))

    def color(self, string: str) -> str:
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
