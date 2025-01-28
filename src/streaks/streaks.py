from collections import Counter
from typing import List

from pydantic import NonNegativeInt, PositiveInt


class Streaks:
    """
    Represent a sequence of integers as a sequence of streaks.

    A streak is a sequence of numbers such that the first number is the smallest.
    The output is a list of such streaks.
    """

    def __init__(self, ints: List[int], losing: bool = False):
        """
        Initialize a Lifts instance.

        Args:
            ints: A list of ints to decompose into streaks.
        """
        self.streaks = self.decompose_into_streaks(ints, losing)

    @property
    def streak_lengths(self) -> Counter:
        """
        Compute the lengths of each streak in the list of streaks.

        Returns:
            Counter: A Counter object where keys are the lengths of the streaks and
            values are the frequency of each length, sorted by length.
        """
        counter = Counter(len(streak) for streak in self.streaks)
        return Counter(dict(sorted(counter.items())))

    @property
    def fixed_points(self) -> NonNegativeInt:
        """
        The number of streaks which are a single element, i.e., are fixed points.

        Returns:
            PositiveInt: The number of streaks which are a single element.
        """
        return self.streak_lengths[1]

    @property
    def streak_count(self) -> PositiveInt:
        """
        The number of streaks in the list of streaks.

        Returns:
            PositiveInt: The number of streaks in the list of streaks.
        """
        return len(self.streaks)

    def decompose_into_streaks(
        self, seq: List[int], losing: bool = False
    ) -> List[List[int]]:
        """
        Decompose a sequence into its component streaks.

        A streak is a sequence of numbers such that the first number is the smallest.
        The output is a list of such streaks.
        If losing is True, the sequence will be decomposed into losing streaks,
        i.e., the first number will be the largest. (Default is False, as in English.
        "He's on a streak." is normally taken to mean "He's on a winning streak.")

        Args:
            seq (list[int]): The sequence to decompose into streaks

        Returns:
            list[list[int]]: A list of streaks
        """
        if not seq:
            return []

        streaks = []
        current_streak = [seq[0]]
        current_streak_start = current_streak[0]

        for i in range(1, len(seq)):
            next_ = seq[i]
            if ((not losing) and (next_ > current_streak_start)) or (
                losing and (next_ < current_streak_start)
            ):
                current_streak.append(next_)
            else:
                streaks.append(current_streak)
                current_streak = [next_]
                current_streak_start = next_

        streaks.append(current_streak)
        return streaks

    def print_streaks(self) -> None:
        """
        Print all streaks in the list of streaks.

        Each streak is printed on its own line, with elements separated by a
        space. The first element of each streak is formatted in green.
        """
        for streak in self.streaks:
            print(self.format_streak(streak))

    def format_streak(self, streak: list[int]) -> str:
        """
        Format a streak.
        Elements are separated by a space.
        First streak element is in green.

        Args:
            streak (list[int]): The list of ints to print
        """
        if not streak:
            return ""
        streak[0] = self.color(streak[0])
        return " ".join(map(str, streak))

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
