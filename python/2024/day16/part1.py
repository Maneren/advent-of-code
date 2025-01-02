from typing import Callable
from queue import PriorityQueue

DIRECTION_MAP = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


def dijkstra(grid, start, end):
    queue = PriorityQueue()

    values = {start: 0}
    queue.put((0, start, ">"))

    while queue:
        value, pos, incoming_direction = queue.get()

        if pos == end:
            return values[pos]

        for direction, (dx, dy) in DIRECTION_MAP.items():
            x, y = pos
            new_pos = nx, ny = x + dx, y + dy

            if grid[ny][nx] == "#":
                continue

            new_value = value + 1 + 1000 * (direction != incoming_direction)

            if new_pos not in values or value > new_value:
                values[new_pos] = new_value
                queue.put((new_value, new_pos, direction))


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    grid = [list(line) for line in lines]

    print("\n".join("".join(line) for line in grid))

    position = next(
        (x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "S"
    )

    end = next(
        (x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "E"
    )

    print(position)
    print(end)

    distance = dijkstra(grid, position, end)
    print_output(distance)
