from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    grid = list(map(list, open(0).read().splitlines()))

    first, rest = grid[0], grid[1:]

    start = first.index("S")

    active = [False] * len(first)
    active[start] = True

    splits = 0

    for line in rest:
        for i, c in enumerate(line):
            if c == "^" and active[i]:
                splits += 1
                active[i] = False
                active[i + 1] = True
                active[i - 1] = True

    print_output(splits)
