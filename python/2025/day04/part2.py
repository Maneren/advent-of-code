from typing import Callable


NEIGHBORS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    grid = [[ch == "@" for ch in line] for line in lines]


    total = 0

    while True:
        to_remove = []

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if not grid[y][x]:
                    continue

                full = 0
                for dx, dy in NEIGHBORS:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx]:
                        full += 1

                if full < 4:
                    to_remove.append((x, y))

        if not to_remove:
            break

        total += len(to_remove)

        for x, y in to_remove:
            grid[y][x] = False

    print_output(total)


