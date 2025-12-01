from days.day01 import solve
from tests.helpers import load_example


def test_day01_example():
    text_input = load_example(1)
    part1, part2 = solve(text_input)

    assert part1 == 42
    assert part2 == 1337
