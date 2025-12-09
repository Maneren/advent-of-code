from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0)

    coords = [tuple(map(int, line.split(","))) for line in lines]

    maximum = max(
        abs(ax - bx + 1) * abs(ay - by + 1)
        for i, (ax, ay) in enumerate(coords)
        for (bx, by) in coords[i + 1 :]
    )

    print_output(maximum)
