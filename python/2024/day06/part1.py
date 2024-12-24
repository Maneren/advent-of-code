from typing import Callable

DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def solve(print: Callable, print_output: Callable) -> None:
    lines = list(map(list, open(0).read().splitlines()))
    guard = None

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "^":
                guard = (j, i)

    print(guard)

    dir_i = 0

    x, y = guard

    counter = 0

    while 0 <= y < len(lines) and 0 <= x < len(lines[0]):
        if lines[y][x] != "X":
            counter += 1
            lines[y][x] = "X"

        for dir in range(dir_i, dir_i + 4):
            direction = DIRECTIONS[dir % 4]

            dx = x + direction[0]
            dy = y + direction[1]

            if dx < 0 or dx >= len(lines[0]) or dy < 0 or dy >= len(lines):
                x = dx
                y = dy
                break

            if lines[dy][dx] == "#":
                continue

            dir_i = dir

            print(x, y, " -> ", dx, dy, f"({dir_i} = {DIRECTIONS[dir_i%4]}])")
            x = dx
            y = dy

            break

    print("\n".join("".join(line) for line in lines))
    print_output(counter)
