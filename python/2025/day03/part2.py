import functools
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    banks = [tuple(map(int, line))[::-1] for line in lines if line]

    total = 0

    for bank in banks:
        @functools.cache
        def find_best(bank: tuple[int, ...], pos: int, take: int) -> int:
            if take == 1:
                return max(bank[pos:])

            best = 0
            for i in range(pos, len(bank) - take + 1):
                val = bank[i]
                current = val + find_best(bank,  i + 1, take - 1) * 10
                best = max(best, current)

            return best

        best = 0
        for j in range(len(bank) - 11):
            best = max(best, find_best(bank, j, 12))

        total += best

    print_output(total)
