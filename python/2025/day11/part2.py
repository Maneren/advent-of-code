import functools
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    graph = {}

    for line in lines:
        a, b = line.strip().split(":")
        graph[a] = b.strip().split()

    @functools.cache
    def count_paths(start, end, dac: bool, fft: bool):
        if start == end:
            return int(dac and fft)

        if start == "dac":
            dac = True

        if start == "fft":
            fft = True

        total = 0

        for node in graph[start]:
            total += count_paths(node, end, dac, fft)

        return total

    print_output(count_paths("svr", "out", False, False))
