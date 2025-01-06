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
    queue.put((0, t := 0, start, [start]))

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

    shortcut_targets = [
        y + x * 1j
        for x in range(-20, 21)
        for y in range(-20, 21)
        if 2 <= abs(x) + abs(y) <= 20
    ]

    shortcuts = sum(
        tiles[new_tile] - index - abs(move.real) - abs(move.imag) > 100
        for tile, index in tiles.items()
        for move in shortcut_targets
        if (new_tile := tile + move) in tiles
    )

    print_output(shortcuts)
