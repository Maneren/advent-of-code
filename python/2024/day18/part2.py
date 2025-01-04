from collections import defaultdict
from queue import PriorityQueue
from typing import Callable

SIZE = 71


def dijkstra(grid, start, end):
    visited = set()

    values = defaultdict(lambda: 1e9)
    queue = PriorityQueue()
    queue.put((0, t := 0, start))

    while not queue.empty():
        value, _, position = queue.get()

        if position in visited:
            continue
        else:
            visited.add(position)

        if position == end:
            return value

        if value > values[position]:
            continue
        else:
            values[position] = value

        for move in 1, +1j, -1j, -1:
            new_position = position + move

            if new_position not in grid or grid[new_position]:
                continue

            queue.put(
                (
                    value + 1,
                    t := t + 1,
                    new_position,
                )
            )

    return None


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    kilobyte = coords[:1024]

    grid = {x + y * 1j: 0 for x in range(SIZE) for y in range(SIZE)}

    for x, y in kilobyte:
        grid[x + y * 1j] = 1

    end = (SIZE - 1) * (1 + 1j)

    for x, y in coords[1024:]:
        grid[x + y * 1j] = 1
        if dijkstra(grid, 0, end) is None:
            print_output(f"{x},{y}")
            return
