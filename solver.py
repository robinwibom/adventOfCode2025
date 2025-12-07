import importlib
from argparse import ArgumentParser
from fetch_inputs import fetch_input
from pathlib import Path

def load_text(day: int, example: bool) -> str:
    folder = Path("data") / f"day{day:02d}"
    file = folder / ("example.txt" if example else "input.txt")
    if not file.exists():
        raise FileNotFoundError
    return file.read_text().strip()

def main():
    parser = ArgumentParser()
    parser.add_argument("--day", type=int, help="Day number to solve (defaults to today if December)")
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--part", choices=["a", "b"], help="Solve only part A or B")
    args = parser.parse_args()

    day = args.day
    
    if day is None:
        from datetime import datetime
        now = datetime.now()
        if now.month == 12 and 1 <= now.day <= 12:
            day = now.day
            print(f"No day specified. Defaulting to today: Day {day}")
        else:
            print("Error: No day specified and today is not an Advent of Code day (Dec 1-12).")
            return

    try:
        module = importlib.import_module(f"days.day{day:02d}")
    except ModuleNotFoundError:
        print(f"Error: The file 'days/day{day:02d}.py' does not exist.")
        print(f"Run 'uv run python scaffold.py --day {day}' to create it.")
        return
    
    if not hasattr(module, "solve"):
        print(f"Error: The solution for day{day:02d}.py must define a solve(text_input) function.")
        return
    
    try:
        text_input = load_text(day, example=args.example)
    except FileNotFoundError:
        print(f"Input file not found for Day {day}. Fetching...")
        try:
            fetch_input(day)
            text_input = load_text(day, example=args.example)
        except Exception as e:
            print(f"Error fetching input: {e}")
            return

    import time

    start_time = time.perf_counter()
    part1, part2 = module.solve(text_input)
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    
    print(f"=== Day {day:02d} ===")
    print(f"Input: {'example' if args.example else 'real'}")

    if args.part == "a":
        print("Part 1:", part1)
    elif args.part == "b":
        print("Part 2:", part2)
    else:
        print("Part 1:", part1)
        print("Part 2:", part2)
        
    print(f"\nTime: {duration:.4f}s")


if __name__ == "__main__":
    main()

