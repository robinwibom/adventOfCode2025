def solution_1(id_range: str) -> int:
    start, stop = map(int, id_range.split("-"))
    total = 0

    for value in range(start, stop + 1):
        s = str(value)

        # Only possible if the length is even
        if len(s) % 2 != 0:
            continue

        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            total += value

    return total


def solution_2(id_range: str) -> int:
    start, stop = map(int, id_range.split("-"))
    total = 0

    for value in range(start, stop + 1):
        s = str(value)
        n = len(s)

        for L in range(1, n):  # try all possible repeating unit lengths
            if n % L != 0:  # unit length must divide total length
                continue

            unit = s[:L]
            reps = n // L

            if unit * reps == s:
                total += value
                break

    return total


def solve(text: str):
    p1 = 0
    p2 = 0

    for id_range in text.split(","):
        p1 += solution_1(id_range)
        p2 += solution_2(id_range)

    return p1, p2
