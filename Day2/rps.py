def run_rps_day1(strategy):
    rounds = []
    for line in strategy.splitlines():
        if line:
            player2, player1 = line.split()
            p1_map = {"X": "R", "Y": "P", "Z": "S"}
            p2_map = {"A": "R", "B": "P", "C": "S"}
            play1 = RPS.Play(p1_map[player1])
            play2 = RPS.Play(p2_map[player2])
            rounds.append(RPS.Round(play1, play2).score)
    return rounds


def run_rps_day2(strategy):
    rounds = []
    for line in strategy.splitlines():
        if line:
            player2, player1 = line.split()
            p1_map = {
                "X": {"R": "S", "P": "R", "S": "P"},
                "Y": {"R": "R", "P": "P", "S": "S"},
                "Z": {"R": "P", "P": "S", "S": "R"},
            }
            p2_map = {"A": "R", "B": "P", "C": "S"}
            play1 = RPS.Play(p1_map[player1][p2_map[player2]])
            play2 = RPS.Play(p2_map[player2])
            print(play1, play2)
            rounds.append(RPS.Round(play1, play2).score)
    return rounds


class RPS:
    class Play:
        def __init__(self, play):
            self.play = play

        def __repr__(self):
            return f"Play({self.play})"

        @property
        def value(self):
            return {"R": 1, "P": 2, "S": 3}[self.play]

    class Round:
        def __init__(self, play1, play2):
            self._play1 = play1
            self._play2 = play2

        @property
        def score(self):
            return self._play1.value + self.win_lose_draw()

        def win_lose_draw(self):
            if self._play1.play == self._play2.play:
                return 3  # draw
            if self.is_win(self._play1.play, self._play2.play):
                return 6  # win
            else:
                return 0  # lose

        @staticmethod
        def is_win(play, other_play):
            return {
                "R": "S",
                "P": "R",
                "S": "P",
            }[play] == other_play


if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        strategy = f.read()
    rounds = run_rps_day1(strategy)
    print(len(rounds))
    print(sum(rounds))
