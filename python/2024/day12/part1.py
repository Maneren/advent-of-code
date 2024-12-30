from typing import Callable
import sys

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def flood_fill(grid, x, y, queue, visited) -> tuple[int, int]:
    if (x, y) in visited:
        return 0, 0

    perimeter = 0
    area = 1

    current = grid[y][x]
    visited.add((x, y))

    for direction in DIRECTIONS:
        nx, ny = x + direction[0], y + direction[1]

        out_of_bounds = False
        if nx < 0 or nx >= len(grid):
            perimeter += 1
            out_of_bounds = True
        if ny < 0 or ny >= len(grid):
            perimeter += 1
            out_of_bounds = True

        if out_of_bounds:
            continue

        if grid[ny][nx] != current:
            queue.append((nx, ny))
            perimeter += 1
            continue

        new_perimeter, new_area = flood_fill(grid, nx, ny, queue, visited)
        perimeter += new_perimeter
        area += new_area

    return perimeter, area


def solve(print: Callable, print_output: Callable) -> None:
    lines = list(map(list, open(0).read().splitlines()))

    visited = set()
    queue = [(0, 0)]

    total = 0

    while queue:
        x, y = queue.pop()
        if (x, y) in visited:
            continue

        perimeter, area = flood_fill(lines, x, y, queue, visited)
        total += perimeter * area

    print_output(total)
