# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management.

1.  **Install dependencies:**

    ```bash
    uv sync
    ```

2.  **Environment Variables:**
    To automatically fetch inputs, you need your Advent of Code session cookie.

    - Find your session cookie (in browser DevTools > Application > Cookies).
    - Paste it into `~/.config/aocd/token`.
    - _Note: `advent-of-code-data` handles this automatically if configured correctly._

## Usage

### Running Solutions

Run the solver script to execute a specific day's solution.

```bash
# Run Day 1
uv run python solver.py --day 1

# Run with example input
uv run python solver.py --day 1 --example
```

If you don't provide a `--day`, it will default to the current day (if the event is active).

### Creating a New Day

Use the scaffold script to generate the template for a new day.

```bash
# Create files for Day 2
uv run python scaffold.py --day 2
```

This will create `days/day02.py`.

## Structure

- `days/`: Solution files (e.g., `day01.py`).
- `data/`: Inputs and example files (downloaded automatically).
- `solver.py`: Main runner script.
- `scaffold.py`: Script to generate new day templates.
