import importlib
from argparse import ArgumentParser
from fetch_inputs import fetch_input
from pathlib import Path

def load_text(day: int, example: bool) -> str:
    # TODO: If paths dont exist, call fetch_input(day)
    folder = Path("data") / f"day{day:02d}"
    file = folder / ("example.txt" if example else "input.txt")
    return file.read_text().strip()

def main():
    parser = ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--part", choices=["a", "b"], help="Solve only part A or B")
    args = parser.parse_args()

    day = args.day

    try:
        module = importlib.import_module(f"days.day{day:02d}")
    except ModuleNotFoundError:
        print(f"Error: The file 'day{day:02d}.py' does not exist.")
        return
    
    if not hasattr(module, "solve"):
        print(f"Error: The solution for day{day:02d}.py must define a solve(text_input) function.")
        return
    
    text_input = load_text(day, example=args.example)
    part1, part2 = module.solve(text_input)

    print(f"=== Day {day:02d} ===")
    print(f"Input: {'example' if args.example else 'real'}")

    if args.part == "a":
        print("Part 1:", part1)
    elif args.part == "b":
        print("Part 2:", part2)
    else:
        print("Part 1:", part1)
        print("Part 2:", part2)


if __name__ == "__main__":
    main()

