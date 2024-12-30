import itertools
from typing import Callable


def parse_button(line: str) -> tuple[int, int]:
    _, xy = line.split(": ")
    x, y = (int(coord.split("+")[1]) for coord in xy.split(", "))
    return x, y


def parse_target(line: str) -> tuple[int, int]:
    _, xy = line.split(": ")
    x, y = (int(coord.split("=")[1]) for coord in xy.split(", "))
    return x, y


def solve(print: Callable, print_output: Callable) -> None:
    total = 0

    done = False

    while not done:
        button_a = parse_button(input())
        button_b = parse_button(input())
        target = parse_target(input())

        try:
            input()
        except EOFError:
            done = True

        options = [
            (i, j)
            for i, j in itertools.product(range(100), range(100))
            if (
                i * button_a[0] + j * button_b[0] == target[0]
                and i * button_a[1] + j * button_b[1] == target[1]
            )
        ]

        if len(options) > 1:
            print(options)

        if not options:
            continue

        total += min(3 * i + j for i, j in options)

    print_output(total)
