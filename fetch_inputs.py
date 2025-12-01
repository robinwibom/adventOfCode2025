from argparse import ArgumentParser
from pathlib import Path
from aocd import get_data
from aocd.models import Puzzle

def fetch_input(day: int, year: int = 2025) -> None:
    folder = Path("data") / f"day{day:02d}"
    folder.mkdir(parents=True, exist_ok=True)

    example_file = folder / "example.txt"
    if not example_file.exists():
        puzzle = Puzzle(year=year, day=day)
        text = puzzle.examples[0].input_data if puzzle.examples else ""
        example_file.write_text(text)
    
    input_file = folder / "input.txt"
    if not input_file.exists():
        text = get_data(day=day, year=year)
        input_file.write_text(text)

def main():
    p = ArgumentParser()
    p.add_argument("--day", type=int, required=True)
    args = p.parse_args()

    fetch_input(args.day)


if __name__ == "__main__":
    main()