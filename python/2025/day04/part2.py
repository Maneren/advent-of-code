from typing import Callable


NEIGHBORS = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]


def solve(print: Callable, print_output: Callable) -> None:
    grid = {
        (x, y)
        for y, line in enumerate(open(0))
        for x, ch in enumerate(line)
        if ch == "@"
    }
    original = grid.copy()

    while to_remove := {
        (x, y)
        for (x, y) in grid
        if sum((x + dx, y + dy) in grid for dx, dy in NEIGHBORS) < 5
    }:
        grid -= to_remove

    print_output(len(original) - len(grid))
