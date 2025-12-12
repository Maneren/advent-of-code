import re
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read()

    blocks = lines.split("\n\n")

    shape_blocks, regions_block = blocks[:-1], blocks[-1]

    shapes = []

    for shape_block in shape_blocks:
        _, shape = shape_block.split("\n", maxsplit=1)

        shape = [[c == "#" for c in line] for line in shape.splitlines()]
        shapes.append(shape)

    regions = [
        (int(a), int(b), tuple(map(int, c.split())))
        for a, b, c in re.findall(r"(\d++)x(\d++): ((?:\d++ ?+)++)", regions_block)
    ]

    valid = 0

    for width, height, required_shapes in regions:
        total_required = 0

        for i, count in enumerate(required_shapes):
            tiles = sum(map(sum, shapes[i]))

            total_required += count * tiles

        if total_required > width * height:
            continue

        valid += 1

    print_output(valid)
