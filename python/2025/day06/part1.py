from math import prod
import re
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    numbers = (re.findall(r"\d+", line) for line in lines[:-1])

    total = sum(
        {"+": sum, "*": prod}[op](map(int, operands))
        for op, operands in zip(re.findall(r"[+*]", lines[-1]), zip(*numbers))
    )

    print_output(total)
