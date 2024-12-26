from itertools import takewhile
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    numbers = list(map(int, list(input().strip())))

    disk = []

    value = True
    i = 0
    counter = 0

    blocks = []
    free_spaces = []

    for n in numbers:
        if value:
            if n > 0:
                disk.extend([i] * n)
                blocks.append((counter, i, n))
            i += 1
            value = False
        else:
            if n > 0:
                disk.extend([None] * n)
                free_spaces.append((counter, n))
            value = True

        counter += n

    for i, x, n in reversed(blocks):
        for space_idx, (j, m) in enumerate(
            takewhile(lambda space: space[0] < i, free_spaces)
        ):
            if m < n:
                continue

            disk[j : j + n] = [x] * n
            disk[i : i + n] = [None] * n
            if m == n:
                del free_spaces[space_idx]
            else:
                free_spaces[space_idx] = (j + n, m - n)

            break

    total = sum(n * i for i, n in enumerate(disk) if n is not None)

    print_output(total)
