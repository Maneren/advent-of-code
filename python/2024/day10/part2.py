from typing import Callable

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def floodfill_trails(grid, x, y) -> int:
    current = int(grid[y][x])

    if current == 9:
        return 1

    ends = 0
    for direction in DIRECTIONS:
        nx, ny = x + direction[0], y + direction[1]

        if not (0 <= nx < len(grid[0]) and 0 <= ny < len(grid)):
            continue

        if int(grid[ny][nx]) == current + 1:
            ends += floodfill_trails(grid, nx, ny)

    return ends


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    grid = [list(line) for line in lines]

    zeros = [
        (x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "0"
    ]

    total = sum(floodfill_trails(grid, x, y) for x, y in zeros)
    print_output(total)
