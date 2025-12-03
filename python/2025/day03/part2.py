import functools
from typing import Callable


@functools.cache
def find_best(bank: tuple[int, ...], pos: int, take: int) -> int:
    if take == 1:
        return max(bank[pos:])

    return max(
        bank[i] + find_best(bank, i + 1, take - 1) * 10
        for i in range(pos, len(bank) - take + 1)
    )


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    banks = (tuple(map(int, reversed(line))) for line in lines if line)

    total = sum(find_best(bank, 0, 12) for bank in banks)

    print_output(total)
