from typing import Callable


NEIGHBORS = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]


def solve(print: Callable, print_output: Callable) -> None:
    grid = {
        (x, y): ch == "@" for y, line in enumerate(open(0)) for x, ch in enumerate(line)
    }

    total = sum(
        roll and sum(grid.get((x + dx, y + dy), False) for dx, dy in NEIGHBORS) < 5
        for (x, y), roll in grid.items()
    )

    print_output(total)
