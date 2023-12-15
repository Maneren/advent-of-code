import itertools


def solve(print, print_output):
    lines = open(0).read().splitlines()

    directions = [{"L": 0, "R": 1}[x] for x in lines[0]]

    mapping = {}

    for line in lines[2:]:
        src, dst = line.split(" = ")

        dst = dst.strip("()").split(", ")

        mapping[src] = dst

    print(mapping)

    steps = 0
    current = "AAA"

    for direction in itertools.cycle(directions):
        current = mapping[current][direction]

        steps += 1

        if current == "ZZZ":
            break

    print_output(steps)
