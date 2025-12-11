from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).readlines()

    graph = {}

    for line in lines:
        a, b = line.strip().split(":")
        graph[a] = b.strip().split()

    def count_paths(start, end):
        if start == end:
            return 1

        total = 0

        for node in graph[start]:
            total += count_paths(node, end)

        return total

    print_output(count_paths("you", "out"))
