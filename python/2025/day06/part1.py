from functools import reduce
import operator
import re
from typing import Callable


def identity(a):
    return a


def strop(op):
    match op:
        case "+":
            return operator.add
        case "*":
            return operator.mul
        case _:
            raise ValueError(op)


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    numbers = [re.findall(r"\d+", line) for line in lines[:-1]]
    ops = map(strop, re.findall(r"[+*]", lines[-1]))

    total = 0

    for j, op in enumerate(ops):
        result = reduce(op, (int(num_line[j]) for num_line in numbers))
        print(result)
        total += result

    print_output(total)
