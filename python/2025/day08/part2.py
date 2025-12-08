from math import dist
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    boxes = [tuple(map(int, line.split(","))) for line in lines]

    distance_pairs = sorted(
        ((a, b) for i, a in enumerate(boxes) for b in boxes[i + 1 :]),
        key=lambda x: dist(*x),
    )

    comp_map = {box: {box} for box in boxes}

    for a, b in distance_pairs:
        a_component = comp_map[a]
        b_component = comp_map[b]

        if a_component == b_component:
            continue

        if len(a_component) < len(b_component):
            a_component, b_component = b_component, a_component

        a_component.update(b_component)

        if len(a_component) == len(boxes):
            print_output(a[0] * b[0])
            break

        for box in b_component:
            comp_map[box] = a_component
