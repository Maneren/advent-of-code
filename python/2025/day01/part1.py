from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    inputs = open(0).read().splitlines()

    total = 50
    counter = 0

    for line in inputs:
        d, n = line[0], int(line[1:])

        sgn = -1 if d == "L" else 1

        total = (total + sgn * n) % 100

        counter += total == 0

    print(total, counter)
    print_output(counter)
