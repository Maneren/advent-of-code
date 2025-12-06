import re
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    blocks = "\n".join(map(str.strip, map("".join, zip(*lines[:-1])))).split("\n\n")
    ops = re.findall(r"[+*]", lines[-1])

    total = sum(eval(op.join(block.splitlines())) for op, block in zip(ops, blocks))

    print_output(total)
