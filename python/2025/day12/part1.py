import re
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    regions_block = open(0).read().split("\n\n")[-1]

    regions = [
        (int(a), int(b), tuple(map(int, c.split())))
        for a, b, c in re.findall(r"(\d++)x(\d++): ((?:\d++ ?+)++)", regions_block)
    ]

    valid = sum(
        9 * sum(required_shapes) <= width * height
        for width, height, required_shapes in regions
    )

    print_output(valid)
