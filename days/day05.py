def solution_1(text: str):
    fresh_ids = []
    expired_ids = []
    counter = 0
    for line in text.splitlines():
        if line:
            counter += 1
            start, stop = map(int, line.split("-"))
            for i in range(start, stop+1):
                if i not in fresh_ids:
                    fresh_ids.append(i)
                    fresh_ids.sort()
        else:
            break
    
    # We now that the id's start on line counter + 1
    counter_2 = 0
    for line in text.splitlines():
        if counter_2 <= counter:
            counter_2 += 1
            continue

        if int(line) not in fresh_ids:
            expired_ids.append(int(line))

    return len(expired_ids)


def solve(input_text: str) -> tuple[int | str, int | str]:
    part2 = 0
    
    return solution_1(input_text), part2