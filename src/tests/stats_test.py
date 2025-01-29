from itertools import permutations

# from streaks.streaks import Streaks


def test_stirling():
    n = 5
    for sequence in permutations(range(n)):
        pass
        # streaks = Streaks(sequence)
        # print_streaks(streaks)
        # for k, count in streak_counts.items():
        #     if count != stirling(n, k, kind=1):
        #         print(f"{k}:{count} is not {stirling(n, k, kind=1)}", sys.stderr)
        #         sys.exit()
