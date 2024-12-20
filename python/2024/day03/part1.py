from typing import Callable
from re import findall


def solve(print: Callable, print_output: Callable) -> None:
    i = open(0).read()
    print_output(sum(int(a) * int(b) for a, b in findall(r"mul\((\d+),(\d+)\)", i)))
