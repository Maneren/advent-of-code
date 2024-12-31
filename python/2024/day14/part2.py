from typing import Callable

WIDTH = 101
HEIGHT = 103

DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    robots = []

    for line in lines:
        pos_str, vel_str = line.split(" ")
        pos_str = pos_str.removeprefix("p=")
        vel_str = vel_str.removeprefix("v=")

        pos = tuple(map(int, pos_str.split(",")))
        vel = tuple(map(int, vel_str.split(",")))

        robots.append((pos, vel))

    for frame in range(1, 9000):
        for i, robot in enumerate(robots):
            pos, vel = robot
            pos = (
                (pos[0] + vel[0] + WIDTH) % WIDTH,
                (pos[1] + vel[1] + HEIGHT) % HEIGHT,
            )
            robots[i] = (pos, vel)

        grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

        for pos, _ in robots:
            x, y = pos
            grid[y][x] = "#"

        neighbors = 0

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if grid[y][x] == ".":
                    continue

                for direction in DIRECTIONS:
                    nx, ny = x + direction[0], y + direction[1]

                    if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                        continue

                    if grid[ny][nx] != ".":
                        neighbors += 1

        if neighbors >= 250:
            print("\n".join("".join(row) for row in grid))
            print(frame)
