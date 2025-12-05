from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    ranges, items = map(str.splitlines, open(0).read().split("\n\n"))

    ranges = [tuple(map(int, line.split("-"))) for line in ranges]

    count = sum(any(lo <= item <= hi for lo, hi in ranges) for item in map(int, items))

    print_output(count)
