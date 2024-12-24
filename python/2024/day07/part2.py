from itertools import product
from typing import Callable
from math import log10


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()
    total = 0

    for line in lines:
        target_s, values_s = line.split(": ")

        target = int(target_s)
        values = list(map(int, values_s.split(" ")))

        for combination in product(["+", "*", "||"], repeat=len(values) - 1):
            result = values[0]

            for value, operator in zip(values[1:], combination):
                if operator == "+":
                    result += value
                elif operator == "*":
                    result *= value
                elif operator == "||":
                    result *= 10 ** (int(log10(value)) + 1)
                    result += value
                else:
                    raise ValueError

            if result == target:
                total += target
                break

    print_output(total)
