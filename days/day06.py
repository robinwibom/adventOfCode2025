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
    columns = list(zip(*numbers))

    for col, op in zip(columns, operations):
        print(col)
        max_length = len(str(max(col)))
        # Damn, I can't just naivley padd right...
        padded_numbers = [str(x).rjust(max_length, "X") for x in col]
        print(f"-> {padded_numbers}")
        digit_numbers = []

        for i in range(max_length):
            digits = ""
            for num in padded_numbers:
                if num[i] != "X":
                    digits += num[i]
            if digits:
                digit_numbers.append(int(digits))

        print(f"-> {digit_numbers}")
        if op == "+":
            result += sum(digit_numbers)
        elif op == "*":
            result += math.prod(digit_numbers)

    return result


def solve(input_text: str) -> tuple[int | str, int | str]:
    numbers = [
        list(map(int, row.split())) for row in input_text.strip().splitlines()[:-1]
    ]
    operations = input_text.strip().splitlines()[-1].split()

    return p1(numbers, operations), p2(numbers, operations)
