from typing import Callable

SIZE = 71


def print_grid(print, grid):
    for y in range(SIZE):
        for x in range(SIZE):
            n = x + y * 1j
            print("#" if n in grid and grid[n] else ".", end="")
        print()


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    kilobyte = coords[:1024]

    grid = {x + y * 1j: 0 for x in range(SIZE) for y in range(SIZE)}

    for x, y in kilobyte:
        grid[x + y * 1j] = 1

    print_grid(print, grid)

    end = (SIZE - 1) * (1 + 1j)

    # bfs
    queue = [(0j, 0)]
    seen = set()

    max_dist = 0

    while queue:
        pos, dist = queue.pop(0)

        if dist > max_dist:
            # grid[coords[dist]]
            max_dist = dist

        if pos == end:
            break

        if pos in seen:
            continue

        seen.add(pos)

        for direction in [1, -1, 1j, -1j]:
            new_pos = pos + direction
            if new_pos in grid and grid[new_pos] == 0:
                queue.append((new_pos, dist + 1))

    print_output(max_dist)
