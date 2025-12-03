def solve(text: str):
    invalid_ids = []
    p2 = 0

    id_ranges = text.split(",")
    for id_range in id_ranges:
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

    return sum(invalid_ids), p2
