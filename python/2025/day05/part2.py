from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    ranges = []

    for line in lines:
        if not line:
            break

        a, b = map(int, line.split("-"))
        ranges.append((a, b))

    ranges.sort()

    merged = []

    for a, b in ranges:
        if not merged or merged[-1][1] < a:
            merged.append((a, b))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))

    count = 0

    for a, b in merged:
        count += b - a + 1

    print_output(count)
