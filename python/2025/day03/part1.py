from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    banks = [list(map(int, line)) for line in lines]

    total = 0

    for bank in banks:
        best = 0
        for i, hi in enumerate(bank):
            for lo in bank[i + 1 :]:
                best = max(best, hi * 10 + lo)

        total += best

    print_output(total)
