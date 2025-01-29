from collections import Counter
from operator import gt, lt
from typing import List

from pydantic import NonNegativeInt


class Streaks:
    """
    Represent a sequence of integers as a sequence of streaks.

    A streak is a sequence of numbers such that the first number is the smallest.
    The output is a list of such streaks.
    """

    def __init__(self, sequence: List[int], winning: bool = True) -> None:
        """
        Initialize a Streaks instance.

        Args:
            sequence (List[int]): A list of ints to decompose into streaks.
            winning (bool, optional): Whether to decompose into winning or losing streaks. Defaults to True.
        """
        self.streaks = self.decompose_into_streaks(sequence, winning)

    @property
    def streak_lengths_counter(self) -> Counter:
        """
        Compute the lengths of each streak in the list of streaks.

        Returns:
            Counter: A Counter object where keys are the lengths of the streaks and
            values are the frequency of each length, sorted by length.
        """
        streak_lengths = (len(streak) for streak in self.streaks)
        length_counts = Counter(streak_lengths)
        return Counter(dict(sorted(length_counts.items())))

    @property
    def fixed_points_count(self) -> NonNegativeInt:
        """
        The number of streaks which are a single element, i.e., are fixed points.

        Returns:
            NonNegativeInt: The number of fixed points
        """
        return self.streak_lengths_counter[1]

    @property
    def streak_count(self) -> NonNegativeInt:
        """
        The number of streaks in the list of streaks.

        Returns:
            NonNegativeInt: The number of streaks in the list of streaks.
        """
        return len(self.streaks)

    def decompose_into_streaks(
        self, seq: List[int], winning: bool = True
    ) -> List[List[int]]:
        """
        Decompose a sequence into its component streaks.

        A streak is a sequence of numbers such that the first number is
        the smallest (winning) or largest (losing).
        The output is a list of such streaks.
        If winning is False, the sequence will be decomposed into losing streaks,
        i.e., the first number will be the largest. (Default is True, as in English.
        "He's on a streak." is normally taken to mean "He's on a winning streak.")

        Args:
            seq (list[int]): The sequence to decompose into streaks

        Returns:
            list[list[int]]: A list of streaks
        """

        if winning:
            cmp = gt
        else:
            cmp = lt

        if not seq:
            return []

        streaks = []
        current_streak = [seq[0]]
        current_streak_start = current_streak[0]

        for i in range(1, len(seq)):
            next_ = seq[i]
            if cmp(next_, current_streak_start):
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

        Returns:
            None
        """
        for streak in self.streaks:
            print(self.format_streak(streak))

    def format_streak(self, streak: list[int]) -> str:
        """
        Format a streak.
        Elements are separated by a space.
        First streak element is in green.

        Args:
            streak (list[int]): The list of integers to format

        Returns:
            str: The formatted streak as a string
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
