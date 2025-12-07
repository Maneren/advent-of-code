import functools
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    grid = list(map(list, open(0).read().splitlines()))

    @functools.cache
    def count(x: int, y: int) -> int:
        while y < len(grid) and grid[y][x] != "^":
            y += 1

        if y == len(grid):
            return 1

        options = 0
        for di in (-1, 1):
            if 0 <= x + di < len(grid[y]):
                options += count(x + di, y)

        return options

    start = next(
        (x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "S"
    )

    print(start)

    grid[start[1]][start[0]] = "|"

    options = count(*start)

    print(*grid, sep="\n")

    print_output(options)
