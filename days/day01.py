# Day 01 - Circular Track Position
# Part A: Count how many times we land exactly on position 0 after following
#         movement instructions (R/L) on a circular track of size 100, starting at 50.
# Part B: Count how many times we pass through position 0 (not just land on it)
#         while following the same movement instructions.


def solution_1(text: str) -> int:
    lines = text.splitlines()
    counter = 0
    curr = 50
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        sign = 1 if direction == "R" else -1

        curr = (curr + sign * amount) % 100
        if curr == 0:
            counter += 1
    return counter


def solution_2(text: str) -> int:
    lines = text.splitlines()
    counter = 0
    curr = 50
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        full_laps, remaining = divmod(amount, 100)

        counter += full_laps
        if direction == "R":
            counter += curr + remaining >= 100
            curr = (curr + remaining) % 100
        else:
            counter += curr > 0 and curr - remaining <= 0
            curr = (curr - remaining) % 100
    return counter


def solve(text: str):
    return solution_1(text), solution_2(text)
