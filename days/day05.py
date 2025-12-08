# Day 05 - Fresh ID Ranges
# Part A: Count how many given IDs fall within any of the "fresh" ranges.
# Part B: Count the total number of fresh IDs across all merged ranges.


def parse_input(text: str):
    # split ranges and available IDs
    lines = text.strip().splitlines()
    blank = lines.index("")
    range_lines = lines[:blank]
    id_lines = lines[blank + 1 :]
    return range_lines, id_lines


def parse_ranges(range_lines: list[str]) -> list[tuple[int, int]]:
    # convert "a-b" into (a, b)
    ranges = [tuple(map(int, line.split("-"))) for line in range_lines]
    ranges.sort()
    return ranges


def merge_ranges(ranges: list[tuple[int, int]]) -> list[list[int]]:
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def is_fresh(x: int, merged: list[list[int]]) -> bool:
    for a, b in merged:
        if a <= x <= b:
            return True
        if x < a:
            return False
    return False


def solution_1(text: str) -> int:
    range_lines, id_lines = parse_input(text)
    ranges = parse_ranges(range_lines)
    merged = merge_ranges(ranges)

    # count available IDs that fall into any merged range
    return sum(1 for line in id_lines if is_fresh(int(line), merged))


def solution_2(text: str) -> int:
    range_lines, _ = parse_input(text)
    ranges = parse_ranges(range_lines)
    merged = merge_ranges(ranges)

    # sum lengths of all merged ranges
    return sum(b - a + 1 for a, b in merged)


def solve(text: str):
    return solution_1(text), solution_2(text)
