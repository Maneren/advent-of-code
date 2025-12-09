from itertools import pairwise
from math import dist
from typing import Callable, cast


def line_rectangle_intersection(
    l1: tuple[int, int], l2: tuple[int, int], r1: tuple[int, int], r2: tuple[int, int]
) -> bool:
    l1x, l1y = l1
    l2x, l2y = l2
    r1x, r2x = sorted((r1[0], r2[0]))
    r1y, r2y = sorted((r1[1], r2[1]))

    return not (
        max(l1x, l2x) <= r1x
        or r2x <= min(l1x, l2x)
        or max(l1y, l2y) <= r1y
        or r2y <= min(l1y, l2y)
    )


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    coords = [cast(tuple[int, int], tuple(map(int, line.split(",")))) for line in lines]
    borders = list(pairwise(coords + [coords[0]]))

    sorted_borders = sorted(borders, key=lambda x: dist(*x))

    rectangles = sorted(
        (
            ((abs(u - x) + 1) * (abs(v - y) + 1), (x, y), (u, v))
            for i, (x, y) in enumerate(coords)
            for u, v in coords[i + 1 :]
        ),
        reverse=True,
    )

    area = next(
        area
        for area, a, b in rectangles
        if not any(
            line_rectangle_intersection(*border, a, b) for border in sorted_borders
        )
    )

    print_output(area)
