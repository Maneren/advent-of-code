from itertools import product
from typing import Callable


def lock_heights(lock):
    heights = [0] * len(lock[0])

    for i, line in enumerate(lock[1:-1]):
        for j, char in enumerate(line):
            if char == "#":
                heights[j] = i + 1

    return heights


def key_heights(key):
    heights = [0] * len(key[0])

    for i, line in enumerate(reversed(key[1:-1])):
        for j, char in enumerate(line):
            if char == "#":
                heights[j] = i + 1

    return heights


def solve(print: Callable, print_output: Callable) -> None:
    schematics = list(map(str.splitlines, open(0).read().split("\n\n")))

    locks = (lock_heights(lock) for lock in schematics if lock[0] == "#####")
    keys = (key_heights(key) for key in schematics if key[-1] == "#####")

    print_output(
        sum(
            all(lh + kh <= 5 for lh, kh in zip(lock, key))
            for lock, key in product(locks, keys)
        )
    )
