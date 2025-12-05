from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    ranges = []

    for line in lines:
        if not line:
            break

        a, b = map(int, line.split("-"))
        print(a, b)
        ranges.append((a, b))

    count = 0

    for line in lines[len(ranges) + 1 :]:
        line = int(line)
        print(line)
        for lo, hi in ranges:
            if lo <= line <= hi:
                count += 1
                break

    print_output(count)
