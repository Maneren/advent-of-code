from typing import Callable

WIDTH = 101
HEIGHT = 103


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

    for _ in range(100):
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
        grid[y][x] = str(int(grid[y][x]) + 1) if grid[y][x] != "." else "1"

    for row in grid:
        print("".join(row))

    print()

    quadrants = [[], [], [], []]

    middle_x, middle_y = WIDTH // 2, HEIGHT // 2

    for pos, _ in robots:
        x, y = pos

        if x < middle_x and y < middle_y:
            quadrants[0].append(pos)
        elif x > middle_x and y < middle_y:
            quadrants[1].append(pos)
        elif x < middle_x and y > middle_y:
            quadrants[2].append(pos)
        elif x > middle_x and y > middle_y:
            quadrants[3].append(pos)

    print_output(
        len(quadrants[0]) * len(quadrants[1]) * len(quadrants[2]) * len(quadrants[3])
    )
