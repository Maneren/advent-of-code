from typing import Callable


def find_best(bank: tuple[int, ...], take: int) -> int:
    if take == 1:
        return max(bank)

    i = max(range(len(bank) - take + 1), key=bank.__getitem__)

    return bank[i] + find_best(bank[i + 1 :], take - 1) * 10


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    banks = (tuple(map(int, reversed(line))) for line in lines if line)

    total = sum(find_best(bank, 12) for bank in banks)

    print_output(total)
