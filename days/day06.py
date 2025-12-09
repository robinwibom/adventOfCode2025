import math


def p1(numbers: list[list[int]], operations: list[str]) -> int:
    result = 0
    columns = list(zip(*numbers))

    for col, op in zip(columns, operations):
        if op == "+":
            result += sum(col)
        elif op == "*":
            result += math.prod(col)

    return result


def p2(numbers: list[list[int]], operations: list[str]) -> int:
    result = 0

    blocks = []
    current_block = []
    for row in numbers:
        if all(c == " " for c in row):  # separator block
            blocks.append(current_block)
            current_block = []
        else:
            number = ""
            for c in row:
                number += c
            current_block.append(int(number))

    if current_block:  # need to add last block as well
        blocks.append(current_block)

    for col, op in zip(blocks, operations):
        if op == "+":
            result += sum(col)
        elif op == "*":
            result += math.prod(col)

    return result


def parse_text(text: str):
    lines = text.rstrip("\n").splitlines()[:-1]

    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines]

    numbers = [list(line) for line in padded]

    operations = text.strip().splitlines()[-1].split()

    return list(zip(*numbers)), operations


def solve(input_text: str) -> tuple[int | str, int | str]:
    numbers = [
        list(map(int, row.split())) for row in input_text.strip().splitlines()[:-1]
    ]
    operations = input_text.strip().splitlines()[-1].split()

    numbers2, operations2 = parse_text(input_text)
    return p1(numbers, operations), p2(numbers2, operations2)
