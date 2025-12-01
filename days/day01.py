def solve(text: str):
    lines = text.splitlines()
    curr = 50
    counter = 0
    counter2 = 0
    for line in lines:
        direction = line[0]
        amount = int(line[1:])
        sign = 1 if direction == "R" else -1

        curr = (curr + sign*amount) % 100
        if curr == 0:
            counter += 1

        # counter2 += abs((curr + sign*amount) // 99)

    return counter, counter2