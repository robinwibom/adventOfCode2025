from pathlib import Path

def load_example(day: int) -> str:
    folder = Path("data") / f"day{day:02d}"
    return (folder / "example.txt").read_text().strip()