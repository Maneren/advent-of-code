from math import dist
from typing import Callable

def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    boxes = [tuple(map(int, line.split(","))) for line in lines]

    distance_pairs = sorted(
        ((a, b) for i, a in enumerate(boxes) for b in boxes[i + 1 :]),
        key=lambda x: dist(*x),
    )

    components = [{box} for box in boxes]

    for a, b in distance_pairs:
        a_component = b_component = None

        for component in components:
            a_in = a in component
            b_in = b in component

            if a_in and b_in:
                break

            if b_in:
                b_component = component

            elif a_in:
                a_component = component
        else:
            assert a_component is not None
            assert b_component is not None

            a_component.update(b_component)
            components.remove(b_component)

            if len(components) == 1:
                print_output(a[0] * b[0])
                break
