from itertools import takewhile
from typing import Callable

DIRECTION_MAP = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def in_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def move(grid, current, direction):
    x, y = current
    dx, dy = DIRECTION_MAP[direction]
    nx, ny = x + dx, y + dy

    return (nx, ny) if in_bounds(grid, nx, ny) and grid[ny][nx] != "#" else current


def attempt_move_box(grid, current, direction):
    x, y = current
    dx, dy = DIRECTION_MAP[direction]

    stack = []

    while True:
        nx, ny = x + dx, y + dy

        if grid[ny][nx] == "#":
            return False

        pos = x, y = nx, ny
        stack.append(pos)

        if grid[y][x] == ".":
            break

    for x, y in stack:
        grid[y][x] = "O"

    return True


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    grid_lines = takewhile(lambda line: line != "", lines)
    grid = list(map(list, grid_lines))

    robot = x, y = next(
        (x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "@"
    )

    movements = [c for line in lines[len(grid) + 1 :] for c in line]

    for movement in movements:
        grid[y][x] = "."
        new_robot = nx, ny = move(grid, robot, movement)

        if grid[ny][nx] == "#" or (
            grid[ny][nx] == "O" and not attempt_move_box(grid, new_robot, movement)
        ):
            # abort move
            grid[y][x] = "@"
        else:
            grid[ny][nx] = "@"
            robot = x, y = new_robot

    print("Done")
    print("\n".join("".join(line) for line in grid))

    gps = sum(
        100 * y + x
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "O"
    )
    print_output(gps)
