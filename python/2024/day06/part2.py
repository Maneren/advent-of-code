from copy import deepcopy
from typing import Callable
import sys

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


DIRECTION_SYMBOL = ["∧", ">", "v", "<"]


def in_bounds(lines, x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)


def step(x, y, dir_i) -> tuple[int, int]:
    direction = DIRECTIONS[dir_i % 4]
    return x + direction[0], y + direction[1]


def move(lines, x, y, dir_i) -> tuple[int, int, int]:
    for dir in range(dir_i, dir_i + 4):
        dx, dy = step(x, y, dir)

        if not in_bounds(lines, dx, dy) or lines[dy][dx] not in ["#", "O"]:
            return dx, dy, dir % 4

    raise ValueError("Could not move")


def would_loop(lines, dir_i, x, y, visited):
    visited = deepcopy(visited)

    while in_bounds(lines, x, y):
        if (x, y, dir_i) in visited:
            return True

        visited.add((x, y, dir_i))

        x, y, dir_i = move(lines, x, y, dir_i)

    return False


def solve(print: Callable, print_output: Callable) -> None:
    lines = list(map(list, open(0).read().splitlines()))
    guard = None

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                guard = (j, i)

    x, y = guard
    dir_i = 0
    lines[y][x] = str(dir_i)

    visited = set()
    possible_places = set()

    while in_bounds(lines, x, y):
        if lines[y][x] == ".":
            lines[y][x] = DIRECTION_SYMBOL[dir_i % 4]

        visited.add((x, y, dir_i))

        for dir in range(dir_i, dir_i + 4):
            ox, oy = obstacle = step(x, y, dir)

            if lines[oy][ox] != "#":
                break

        else:
            raise ValueError("Could not place obstacle")

        if (
            obstacle != guard
            and obstacle not in possible_places
            and all((ox, oy, d % 4) not in visited for d in range(dir_i, dir_i + 4))
        ):
            lines[oy][ox] = "O"
            if would_loop(lines, dir + 1, x, y, visited):
                possible_places.add(obstacle)
            lines[oy][ox] = "."

        x, y, dir_i = move(lines, x, y, dir_i)

    print("\n".join("".join(line) for line in lines))
    print_output(len(possible_places))
