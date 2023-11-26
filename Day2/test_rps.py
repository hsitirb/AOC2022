import pytest
from rps import run_rps, RPS


@pytest.mark.parametrize(
    "strategy, expected",
    [
        ("A Y\nB X\nC Z", 15),
    ],
)
def test_rps_part1(strategy, expected):
    assert run_rps(strategy) == expected


@pytest.mark.parametrize(
    "entry, expected",
    [
        ("R", 1),
        ("P", 2),
        ("S", 3),
    ],
)
def test_rps_play_value(entry, expected):
    assert RPS.Play(entry).value == expected


@pytest.mark.parametrize(
    "player1, player2, expected",
    [
        ("R", "R", 1 + 3),
        ("R", "P", 1 + 0),
        ("R", "S", 1 + 6),
        ("P", "R", 2 + 6),
        ("P", "P", 2 + 3),
        ("P", "S", 2 + 0),
        ("S", "R", 3 + 0),
        ("S", "P", 3 + 6),
        ("S", "S", 3 + 3),
    ],
)
def test_rps_play(player1, player2, expected):
    play1 = RPS.Play(player1)
    play2 = RPS.Play(player2)
    assert RPS.Round(play1, play2).score == expected
