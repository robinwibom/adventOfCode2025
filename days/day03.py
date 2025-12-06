def solution_1(line: str) -> int:
    digits =[int(c) for c in line]
    n = len(digits)

    best_right = [-1] * n
    best = -1

    # build best_right by using backwardspass
    for i in range(n - 1, -1, -1):
        best_right[i] = best
        best = max(best, digits[i])
    
    best_pair = -1

    # compute best two-digit number for each position
    for i in range(n):
        if best_right[i] == -1:
            continue
        candidate = digits[i] * 10 + best_right[i]
        best_pair = max(best_pair, candidate)
        
    return best_pair

def solution_2(line: str) -> int:
    digits = [int(c) for c in line]
    k = 12
    n = len(digits)

    chosen = []
    start = 0

    for pick in range(k):
        # how many digits remain to pick after this one
        remaining = k - pick - 1

        # last index we are allowed to start from
        # we must leave enough digits for the rest
        end = n - remaining

        # pick the largest digit in digits[start:end]
        best_digit = -1
        best_index = -1

        for i in range(start, end):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_index = i

        chosen.append(best_digit)
        start = best_index + 1

    weights = [10 ** exp for exp in range(k - 1, -1, -1)]
    value = sum(d * w for d, w in zip(chosen, weights))

    return value


def solve(text: str):
    p1 = 0
    p2 = 0

    for line in text.splitlines():
        p1 += solution_1(line)
        p2 += solution_2(line)

    return p1, p2