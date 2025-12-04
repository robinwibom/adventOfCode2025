def solution_1(id_range: str) -> int:
    invalid_ids = []

    start_id = int(id_range.split("-")[0])
    stop_id = int(id_range.split("-")[-1])

    value_range = stop_id - start_id

    for i in range(0, value_range + 1):
        id = str(start_id + i)

        if len(id) % 2 == 0:
            firstpart, secondpart = id[: len(id) // 2], id[len(id) // 2 :]
            if firstpart == secondpart:
                invalid_id = firstpart + secondpart
                invalid_ids.append(int(invalid_id))

    return sum(invalid_ids)


def generate_substrings(string: str) -> list[str]:
    substrings = []
    for i in range(1, len(string) + 1):
        substrings.append(string[:i])
        # print(substrings[-1])
    return substrings


def solution_2(id_range: str) -> int:
    invalid_ids = []

    start_id = int(id_range.split("-")[0])
    stop_id = int(id_range.split("-")[-1])

    value_range = stop_id - start_id
    for i in range(0, value_range + 1):
        id = str(start_id + i)
        n = len(id)
        print(f"--- {id} ---")

        for L in range(1, n):
            if n % L != 0:
                continue
            s = id[:L]
            mult = n // L
            if s * mult == id:
                invalid_ids.append(int(id))
                break

    return sum(invalid_ids)


def solve(text: str):
    p1 = 0
    p2 = 0

    id_ranges = text.split(",")
    for id_range in id_ranges:
        # p1 += solution_1(id_range)
        p2 += solution_2(id_range)

    return p1, p2
