from collections import defaultdict
from typing import Callable


def solve(print: Callable, print_output: Callable) -> None:
    edges = (line.split("-") for line in open(0).read().splitlines())

    graph = defaultdict(set)

    for src, dst in edges:
        graph[src].add(dst)
        graph[dst].add(src)

    def clique_from(vertex: str):
        clique = [vertex]

        for neighbor in graph[vertex]:
            if neighbor not in clique and all(neighbor in graph[v] for v in clique):
                clique.append(neighbor)

        return tuple(clique)

    print_output(",".join(sorted(max(map(clique_from, graph), key=len))))
