from collections import deque
from math import prod, sqrt
from typing import Callable

def distance(a, b):
    return sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(a, b)))

def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    boxes = [tuple(map(int, line.split(","))) for line in lines]

    distance_pairs = sorted(
        (distance(a, b), a, b) for i, a in enumerate(boxes) for b in boxes[i + 1 :]
    )

    graph = {box: set() for box in boxes}

    for _, a, b in distance_pairs[:1000]:
        graph[a].add(b)
        graph[b].add(a)

    # find components
    components = []
    visited = set()
    queue = deque()

    for box in graph:
        if box in visited:
            continue

        components.append([])
        queue.append(box)

        while queue:
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            components[-1].append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print_output(prod(sorted(map(len, components))[-3:]))
