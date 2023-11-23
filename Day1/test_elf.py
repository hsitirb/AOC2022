import pytest
from elf import elf_with_max_calories

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
expected = 24000

@pytest.mark.parametrize("input, expected", [[sample_input, expected]])
def test_elf(input, expected):
    assert elf_with_max_calories(input) == expected

