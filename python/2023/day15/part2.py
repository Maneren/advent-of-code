from typing import Callable


def aoc_hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256

    return value


def solve(print: Callable, print_output: Callable) -> None:
    line = open(0).read().strip()

    steps = line.split(",")

    boxes: list[dict[str, int]] = [{} for _ in range(256)]

    for step in steps:
        if step.endswith("-"):
            key = step[:-1]
            box = boxes[aoc_hash(key)]
            if key in box:
                del box[key]
        else:
            key, value = step.split("=")
            box = boxes[aoc_hash(key)]
            box[key] = int(value)

    total = sum(
        sum(
            (box_index + 1) * (slot + 1) * focal_length
            for slot, focal_length in enumerate(box.values())
        )
        for box_index, box in enumerate(boxes)
    )

    print_output(total)
