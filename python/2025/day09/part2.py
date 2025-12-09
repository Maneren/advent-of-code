from itertools import pairwise
from math import dist
from typing import Callable, cast


def line_rectangle_intersection(
    l1: tuple[int, int], l2: tuple[int, int], r1: tuple[int, int], r2: tuple[int, int]
) -> bool:
    l1x, l1y = l1
    l2x, l2y = l2
    r1x, r1y = r1
    r2x, r2y = r2

    return (
        max(l1x, l2x) > min(r1x, r2x)
        and min(l1x, l2x) < max(r1x, r2x)
        and max(l1y, l2y) > min(r1y, r2y)
        and min(l1y, l2y) < max(r1y, r2y)
    )


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    coords = [cast(tuple[int, int], tuple(map(int, line.split(",")))) for line in lines]

    borders = pairwise(coords + [coords[0]])
    # longer borders have higher chance of intersection, so we will check them first
    sorted_borders = sorted(borders, key=lambda x: dist(*x), reverse=True)

    rectangles = (
        ((abs(bx - ax) + 1) * (abs(by - ay) + 1), (ax, ay), (bx, by))
        for i, (ax, ay) in enumerate(coords)
        for bx, by in coords[i + 1 :]
    )

    area = next(
        area
        for area, a, b in sorted(rectangles, reverse=True)
        if not any(
            line_rectangle_intersection(*border, a, b) for border in sorted_borders
        )
    )

    print_output(area)
