from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    coords = [tuple(map(int, line.split(","))) for line in lines]

    maximum = 0

    for i, a in enumerate(coords):
        for b in coords[i + 1 :]:
            area = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
            maximum = max(maximum, area)

    print_output(maximum)
