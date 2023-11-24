import pytest
from elf import elf_with_max_calories, top3_elves_with_max_calories

sample_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
expected1 = 24000
expected2 = 45000


@pytest.mark.parametrize("input, expected", [[sample_input, expected1]])
def test_elf_part1(input, expected):
    assert elf_with_max_calories(input) == expected


@pytest.mark.parametrize("input, expected", [[sample_input, expected2]])
def test_elf_part2(input, expected):
    assert top3_elves_with_max_calories(input) == expected
