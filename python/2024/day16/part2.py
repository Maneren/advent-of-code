from collections import defaultdict
from typing import Callable
from queue import PriorityQueue


def dijkstra(grid, start, end):
    visited = set()
    best = 1e9

    values = defaultdict(lambda: 1e9)
    queue = PriorityQueue()
    queue.put((0, t := 0, start, 1j, [start]))

    while not queue.empty():
        value, _, position, direction, path = queue.get()

        if value > values[position, direction]:
            continue
        else:
            values[position, direction] = value

        if position == end and value <= best:
            visited.update(path)
            best = value

        for move, new_value in (1, 1), (+1j, 1001), (-1j, 1001):
            new_position = position + direction * move

            if new_position not in grid:
                continue

            new_value = value + new_value
            new_direction = direction * move

            queue.put(
                (
                    new_value,
                    t := t + 1,
                    new_position,
                    new_direction,
                    path + [new_position],
                )
            )

    return best, visited


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    grid = {
        i + j * 1j: char
        for i, row in enumerate(lines)
        for j, char in enumerate(row)
        if char != "#"
    }

    start = next(k for k, v in grid.items() if v == "S")
    end = next(k for k, v in grid.items() if v == "E")

    best, visited = dijkstra(grid, start, end)

    print(best)

    print_output(len(visited))
