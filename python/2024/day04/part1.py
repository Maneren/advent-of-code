from re import finditer
from typing import Callable


def rotate(row: list, n: int):
    return row[n:] + row[:n]


def diags(grid: list[str], rev=False):
    n = len(grid)
    _grid = [list(row) + [None] * (n - 1) for row in grid]  # pad for rotation
    for diag in zip(*(rotate(_grid[i], (i, -i)[rev]) for i in range(n))):
        d = "".join(filter(None, diag))
        yield from (d, d[::-1])
    if not rev:
        yield from diags(grid, rev=True)


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    total = 0

    # horizontal

    for line in lines:
        total += sum(1 for _ in finditer("XMAS", line))
        total += sum(1 for _ in finditer("SAMX", line))

    # vertical

    for column in zip(*lines):
        column_str = "".join(column)
        total += sum(1 for _ in finditer("XMAS", column_str))
        total += sum(1 for _ in finditer("SAMX", column_str))

    # diagonals

    for diag in diags(lines):
        total += sum(1 for _ in finditer("XMAS", diag))

    print_output(total)
