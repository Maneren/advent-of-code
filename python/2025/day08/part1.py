from math import dist, prod, sqrt
from typing import Callable


def distance(a, b):
    return sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(a, b)))


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    boxes = [tuple(map(int, line.split(","))) for line in lines]

    distance_pairs = sorted(
        ((a, b) for i, a in enumerate(boxes) for b in boxes[i + 1 :]),
        key=lambda x: dist(*x),
    )

    comp_map = {box: {box} for box in boxes}

    for a, b in distance_pairs[:1000]:
        a_component = comp_map[a]
        b_component = comp_map[b]

        if a_component == b_component:
            continue

        if len(a_component) < len(b_component):
            a_component, b_component = b_component, a_component

        a_component.update(b_component)
        for box in b_component:
            comp_map[box] = a_component

    print_output(prod(sorted(map(len, set(map(tuple, comp_map.values()))))[-3:]))
