def run_rps(strategy):
    rounds = []
    for line in strategy.splitlines():
        if line:
            player1, player2 = line.split()
            p1_map = {"A":"R", "B":"P", "C":"S"}
            p2_map = {"X":"R", "Y":"P", "Z":"S"}
            play1 = RPS.Play(p1_map[player1])
            play2 = RPS.Play(p2_map[player2])
            rounds.append(RPS.Round(play1, play2).score)
    return sum(rounds)


class RPS:
    class Play:
        def __init__(self, play):
            self.play = play

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
            
