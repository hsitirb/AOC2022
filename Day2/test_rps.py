import pytest
from rps import run_rps_day1, run_rps_day2, RPS


@pytest.mark.parametrize(
    "strategy, expected",
    [
        ("A Y\nB X\nC Z", 15),
    ],
)
def test_rps_part1(strategy, expected):
    assert sum(run_rps_day1(strategy)) == expected

@pytest.mark.parametrize(
    "strategy, expected",
    [
        ("A Y\nB X\nC Z", 12),
    ],
)
def test_rps_part2(strategy, expected):
    assert sum(run_rps_day2(strategy)) == expected


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

def test_win():
    assert RPS.Round.is_win("R", "S")
    assert RPS.Round.is_win("P", "R")
    assert RPS.Round.is_win("S", "P")
    assert not RPS.Round.is_win("S", "S")
    assert not RPS.Round.is_win("R", "P")
    assert not RPS.Round.is_win("P", "S")

def test_win_lose_draw():
    assert RPS.Round(RPS.Play("R"), RPS.Play("R")).win_lose_draw() == 3
    assert RPS.Round(RPS.Play("R"), RPS.Play("S")).win_lose_draw() == 6
    assert RPS.Round(RPS.Play("S"), RPS.Play("R")).win_lose_draw() == 0

def test_score():
    assert RPS.Round(RPS.Play("P"), RPS.Play("R")).score == 8
    assert RPS.Round(RPS.Play("R"), RPS.Play("P")).score == 1
    assert RPS.Round(RPS.Play("S"), RPS.Play("S")).score == 6