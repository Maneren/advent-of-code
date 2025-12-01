import math
from time import sleep
from typing import Callable
import sys

# note: # of sides == # of corners

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def isnt_perpendicular(a, b):
    return a is None or b is None or (a[0] * b[0] + a[1] * b[1]) != 0

def move(x, y, direction):
    return x + direction[0], y + direction[1]

def in_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def count_corners(grid, x, y, shape) -> int:
    s = 0

    for l, r in zip(DIRECTIONS, DIRECTIONS[1:] + DIRECTIONS[:1]):
        left = move(x, y, l)
        right = move(x, y, r)
        diagonal = move(*move(x, y, l), r)

        d_in_grid = in_bounds(grid, diagonal[0], diagonal[1])

        if (left not in shape and right not in shape) or (
            left in shape and right in shape and d_in_grid and diagonal not in shape
        ):
            s += 1

    return s

def flood_fill(grid, x, y, queue, visited, shape):
    if (x, y) in visited:
        return 0

    current = grid[y][x]
    visited.add((x, y))
    shape.add((x, y))

    for direction in DIRECTIONS:
        nx, ny = x + direction[0], y + direction[1]

        if not in_bounds(grid, nx, ny):
            continue

        if grid[ny][nx] != current:
            queue.append((nx, ny))
            continue

        flood_fill(grid, nx, ny, queue, visited, shape)

def solve(print: Callable, print_output: Callable) -> None:
    lines = list(map(list, open(0).read().splitlines()))

    visited = set()
    queue = [(0, 0)]

    total = 0

    while queue:
        x, y = queue.pop()
        if (x, y) in visited:
            continue

        shape = set()
        flood_fill(lines, x, y, queue, visited, shape)
        area = len(shape)
        perimeter = sum(count_corners(lines, x, y, shape) for x, y in shape)
        total += perimeter * area

    print_output(total)
