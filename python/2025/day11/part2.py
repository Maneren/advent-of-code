import functools
from itertools import pairwise, permutations, starmap
from math import prod
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    graph: dict[str, list[str]] = {}

    for line in open(0):
        a, b = line.split(":")
        graph[a] = b.strip().split()

    graph["out"] = []

    @functools.cache
    def count_paths(start: str, end: str):
        return start == end or sum(count_paths(node, end) for node in graph[start])

    print_output(
        sum(
            prod(starmap(count_paths, pairwise(["svr", *nodes, "out"])))
            for nodes in permutations(("fft", "dac"))
        )
    )
