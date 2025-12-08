def p1(numbers: list[list[int]], operations: list[str]) -> int:
    sum = 0
    return sum


def solve(input_text: str) -> tuple[int | str, int | str]:
    part1 = 0
    part2 = 0

    numbers = [
        list(map(int, row.split())) for row in input_text.strip().splitlines()[:-1]
    ]
    operations = input_text.strip().splitlines()[-1].split()

    return p1(numbers, operations), part2
