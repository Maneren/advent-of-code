from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    banks = (list(map(int, line)) for line in lines)

    total = sum(
        max(hi * 10 + lo for i, hi in enumerate(bank) for lo in bank[i + 1 :])
        for bank in banks
    )

    print_output(total)
