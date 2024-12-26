from itertools import takewhile
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    numbers = list(map(int, list(open(0).read().strip())))

    disk = []

    value = True
    i = 0

    for n in numbers:
        if value:
            disk.extend([i] * n)
            i += 1
            value = False
        else:
            disk.extend([None] * n)
            value = True

    i, j = 0, len(disk) - 1

    while i < j:
        while disk[i] is not None:
            i += 1
        while disk[j] is None:
            j -= 1

        disk[i], disk[j] = disk[j], disk[i]

        i += 1
        j -= 1

    total = sum(n * i for i, n in enumerate(takewhile(lambda x: x is not None, disk)))

    print_output(total)
