from typing import Callable


def aoc_hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value %= 256

    return value


def solve(print: Callable, print_output: Callable) -> None:
    line = open(0).read().strip()

    steps = line.split(",")

    accumulator = sum(map(aoc_hash, steps))

    print_output(accumulator)
