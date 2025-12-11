import functools
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    graph: dict[str, list[str]] = {}

    for line in open(0):
        a, b = line.split(":")
        graph[a] = b.strip().split()

    @functools.cache
    def count_paths(start: str, end: str):
        return (
            sum(count_paths(node, end) for node in graph[start]) if start != end else 1
        )

    print_output(count_paths("you", "out"))

