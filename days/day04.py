import numpy as np
from scipy.ndimage import convolve

K = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
], dtype=np.int8)


def parse_grid(text: str) -> np.ndarray:
    lines = text.strip().splitlines()
    h = len(lines)
    w = len(lines[0])
    arr = np.zeros((h,w), dtype=np.int8)

    for i, line in enumerate(lines):
        arr[i] = [1 if c == '@' else 0 for c in line]
    
    return arr

def recursive_remove(arr: np.ndarray) -> np.ndarray:
    grid = arr.copy()

    while True:
        neighbors = convolve(grid, K, mode="constant", cval=0)

        # rolls with fewer than 4 neighbors are accessible -> we can remove them
        removable = (grid == 1) & (neighbors < 4)

        # if no rolls can be removed, we are done
        if not removable.any():
            break

        grid[removable] = 0

    return grid

def solution_1(text: str) -> int:
    arr = parse_grid(text)
    neighbor_count = convolve(arr, K, mode="constant", cval=0)
    accessible = (arr == 1) & (neighbor_count < 4)
    return accessible.sum()

def solution_2(text: str) -> int:
    arr = parse_grid(text)
    final = recursive_remove(arr)
    removed = (arr == 1) & (final == 0)
    return removed.sum()

def solve(text: str):
    return solution_1(text), solution_2(text)