from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    grid = list(map(list, open(0).read().splitlines()))

    first, rest = grid[0], grid[1:]

    start = first.index("S")

    counts = [1] * len(first)
    for line in reversed(rest):
        for i, c in enumerate(line):
            if c == "^":
                counts[i] = counts[i - 1] + counts[i + 1]

    print_output(counts[start])
