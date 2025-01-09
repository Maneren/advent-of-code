from collections import defaultdict
from typing import Callable


def find_cycles(graph, length):
    def find_cycles_inner(cycle) -> list[list[str]]:
        neighbors = graph[cycle[-1]]

        if len(cycle) == length:
            return [cycle] if cycle[0] in neighbors else []

        assert len(cycle) < length

        return [
            c
            for neighbor in neighbors
            for c in find_cycles_inner(cycle + [neighbor])
            if neighbor not in cycle
        ]

    return [cycle for vertex in graph for cycle in find_cycles_inner([vertex])]


def solve(print: Callable, print_output: Callable) -> None:
    edges = [line.split("-") for line in open(0).read().splitlines()]

    graph = defaultdict(set)

    for src, dst in edges:
        graph[src].add(dst)
        graph[dst].add(src)

    cycles = {
        tuple(sorted(cycle))
        for cycle in find_cycles(graph, 3)
        if any(vertex.startswith("t") for vertex in cycle)
    }

    print_output(len(cycles))
