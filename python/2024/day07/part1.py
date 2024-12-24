from itertools import product
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    total = 0

    for line in lines:
        target_s, values_s = line.split(": ")

        target = int(target_s)
        values = list(map(int, values_s.split(" ")))

        for combination in product(["+", "*"], repeat=len(values) - 1):
            expression = str(values[0])
            for value, operator in zip(values[1:], combination):
                expression = f"({expression} {operator} {value})"

            if eval(expression) == target:
                total += target
                break

    print_output(total)
