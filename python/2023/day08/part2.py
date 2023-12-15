import itertools
import math


def lowerst_common_multiple(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def solve(print, print_output):
    lines = open(0).read().splitlines()

    directions = [{"L": 0, "R": 1}[x] for x in lines[0]]

    starting = []

    mapping = {}

    for line in lines[2:]:
        src, dst = line.split(" = ")

        dst = dst.strip("()").split(", ")

        mapping[src] = dst

        if src.endswith("A"):
            starting.append(src)

    steps = 0

    current = starting

    loops = [-1] * len(starting)

    for direction in itertools.cycle(directions):
        for i, node in enumerate(current):
            if loops[i] != -1:
                continue
            current[i] = mapping[node][direction]

            if current[i].endswith("Z"):
                loops[i] = steps + 1

        steps += 1

        if all(x != -1 for x in loops):
            break

    total = 1

    for n in loops:
        total = lowerst_common_multiple(total, n)

    print_output(total)
