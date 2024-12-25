from itertools import product
from typing import Callable


def is_in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    WIDTH = len(lines[0])
    HEIGHT = len(lines)

    antennas: dict[str, list[tuple[int, int]]] = {}

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((int(i), int(j)))

    antinodes = set()

    for positions in antennas.values():
        for pos1, pos2 in product(positions, repeat=2):
            if pos1 == pos2:
                continue

            diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])

            anti1 = pos1[0] + diff[0], pos1[1] + diff[1]
            anti2 = pos2[0] - diff[0], pos2[1] - diff[1]

            if is_in_bounds(*anti1, WIDTH, HEIGHT):
                antinodes.add(anti1)

            if is_in_bounds(*anti2, WIDTH, HEIGHT):
                antinodes.add(anti2)

    print_output(len(antinodes))
