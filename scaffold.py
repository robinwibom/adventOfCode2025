import argparse
from pathlib import Path

TEMPLATE = """
def solve(input_text: str) -> tuple[int | str, int | str]:
    part1 = 0
    part2 = 0
    
    return part1, part2
"""

def scaffold(day: int):
    days_folder = Path("days")
    days_folder.mkdir(exist_ok=True)
    
    day_file = days_folder / f"day{day:02d}.py"
    if day_file.exists():
        print(f"Day {day} already exists at {day_file}")
        return
        
    day_file.write_text(TEMPLATE.strip())
    print(f"Created template for Day {day} at {day_file}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True, help="Day number to scaffold")
    args = parser.parse_args()
    
    scaffold(args.day)

if __name__ == "__main__":
    main()
