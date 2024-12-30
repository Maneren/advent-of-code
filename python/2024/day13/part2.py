from typing import Callable

OFFSET = 10000000000000
EPSILON = 0.001


def parse_button(line: str) -> tuple[int, int]:
    _, xy = line.split(": ")
    x, y = (int(coord.split("+")[1]) for coord in xy.split(", "))
    return x, y


def parse_target(line: str) -> tuple[int, int]:
    _, xy = line.split(": ")
    x, y = (int(coord.split("=")[1]) + OFFSET for coord in xy.split(", "))
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

        x1, y1 = button_a
        x2, y2 = button_b
        x, y = target

        # manual derivation of the Cramer's rule
        l = (y * x1 - x * y1) // (x1 * y2 - x2 * y1)
        k = (x - x2 * l) // x1

        if k < 0 or l < 0 or k * x1 + l * x2 != x or k * y1 + l * y2 != y:
            continue

        total += 3 * int(k) + int(l)

    print_output(total)
