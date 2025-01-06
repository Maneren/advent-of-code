from collections import defaultdict
from queue import PriorityQueue
from typing import Callable


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

    path = None

    values = defaultdict(lambda: 1e9)
    queue = PriorityQueue()
    queue.put((0, t := 0, start, []))

    while not queue.empty():
        value, _, position, path = queue.get()

        if value > values[position]:
            continue

        values[position] = value

        if position == end:
            break

        for move in 1, -1, 1j, -1j:
            new_position = position + move

            if new_position not in grid:
                continue

            queue.put(
                (
                    value + 1,
                    t := t + 1,
                    new_position,
                    path + [new_position],
                )
            )

    assert path is not None

    tiles = {n: i for i, n in enumerate(path)}

    shortcuts = [
        (tile, move, difference)
        for tile, index in tiles.items()
        for move in [2, -2, +2j, -2j]
        if (new_tile := tile + move) in tiles
        and (difference := tiles[new_tile] - index - 2) > 0
    ]

    print_output(sum(difference >= 100 for _, _, difference in shortcuts))
