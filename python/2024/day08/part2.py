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

            dx, dy = (pos1[0] - pos2[0], pos1[1] - pos2[1])

            for (px, py), k in [(pos1, 1), (pos2, -1)]:
                antinodes.add((px, py))
                ax, ay = antinode = px + k * dx, py + k * dy

                while is_in_bounds(ax, ay, WIDTH, HEIGHT):
                    antinodes.add(antinode)
                    ax, ay = antinode = ax + k * dx, ay + k * dy

    print_output(len(antinodes))
