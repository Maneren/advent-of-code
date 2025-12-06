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

    numbers = lines[:-1]
    ops = map(strop, re.findall(r"[+*]", lines[-1]))

    print(numbers)

    total = 0

    operands = []

    for column in zip(*numbers):
        print(column)
        if all(d == " " for d in column):
            op = next(ops)
            result = reduce(op, operands)
            print(operands, op, "=", result)
            total += result
            operands.clear()
            continue

        power = 1
        operand = 0
        for d in reversed(column):
            if d != " ":
                operand += int(d) * power
                power *= 10

        operands.append(operand)

        power *= 10

    op = next(ops)
    result = reduce(op, operands)
    print(operands, op, "=", result)
    total += result

    print_output(total)
