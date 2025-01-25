from collections import Counter
from typing import List

from pydantic import NonNegativeInt, PositiveInt


class Lifts:
    """
    Represent a sequence of integers as a sequence of lifts.

    A lift is a sequence of numbers such that the first number is the smallest.
    The output is a list of such lifts.
    """

    def __init__(self, ints: List[int]):
        """
        Initialize a Lifts instance.

        Args:
            ints: A list of ints to decompose into lifts.
        """
        self.lifts = self.decompose_into_lifts(ints)

    @property
    def lift_lengths(self) -> Counter:
        """
        Compute the lengths of each lift in the list of lifts.

        Returns:
            Counter: A Counter object where keys are the lengths of the lifts and
            values are the frequency of each length, sorted by length.
        """
        counter = Counter(len(lift) for lift in self.lifts)
        return Counter(dict(sorted(counter.items())))

    @property
    def fixed_points(self) -> NonNegativeInt:
        """
        The number of lifts which are a single element, i.e., are fixed points.

        Returns:
            PositiveInt: The number of lifts which are a single element.
        """
        return self.lift_lengths[1]

    @property
    def lift_count(self) -> PositiveInt:
        """
        The number of lifts in the list of lifts.

        Returns:
            PositiveInt: The number of lifts in the list of lifts.
        """
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
        Print all lifts in the list of lifts.

        Each lift is printed on its own line, with elements separated by a
        space. The first element of each lift is formatted in green.
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
        Color a string (currently, green only).

        Args:
            string (str): The string to convert

        Returns:
            str: The string wrapped in ANSI codes to color it
        """
        color = "\033[92m"  # green
        end = "\033[0m"
        return f"{color}{string}{end}"
