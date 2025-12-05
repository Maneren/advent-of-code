from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    ranges, _ = map(str.splitlines, open(0).read().split("\n\n"))

    ranges = sorted(tuple(map(int, line.split("-"))) for line in ranges)

    highest = 0

    count = sum(
        -max(highest, lo - 1) + (highest := max(highest, hi)) for lo, hi in ranges
    )

    print_output(count)
