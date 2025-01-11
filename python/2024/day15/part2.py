from itertools import takewhile
from typing import Callable
import sys

DIRECTION_MAP = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

TILE_MAP = {
    ".": "..",
    "#": "##",
    "@": "@.",
    "O": "[]",
}


class Box:
    def __init__(self, x, y):
        self.y = y
        self.x1 = x
        self.x2 = x + 1

    def gps(self):
        return self.x1 + 100 * self.y

    def can_move(self, walls, box_grid, direction) -> tuple[bool, list["Box"]]:
        dx, dy = direction
        if any(
            tile in walls
            for tile in (
                (self.x1 + dx, self.y + dy),
                (self.x2 + dx, self.y + dy),
            )
        ):
            return False, []

        other_boxes = {
            box_grid[tile]
            for tile in (
                (self.x1 + dx, self.y + dy),
                (self.x2 + dx, self.y + dy),
            )
            if tile in box_grid and box_grid[tile] != self
        }

        to_move: list["Box"] = [self]

        for other in other_boxes:
            result, boxes = other.can_move(walls, box_grid, direction)
            if not result:
                return False, []

            to_move += boxes

        return True, to_move

    def move(self, grid, box_grid, direction):
        dx, dy = direction
        print("Move", self.x1, self.y, dx, dy, file=sys.stderr)
        grid[self.y][self.x1] = "."
        grid[self.y][self.x2] = "."
        del box_grid[self.x1, self.y]
        del box_grid[self.x2, self.y]

        self.x1 = self.x1 + dx
        self.x2 = self.x2 + dx
        self.y = self.y + dy

        grid[self.y][self.x1] = "["
        grid[self.y][self.x2] = "]"

        box_grid[self.x1, self.y] = self
        box_grid[self.x2, self.y] = self

    def attempt_move(self, grid, walls, box_grid, direction):
        result, to_move = self.can_move(walls, box_grid, direction)
        if result:
            moved = set()
            for box in reversed(to_move):
                if box in moved:
                    continue

                box.move(grid, box_grid, direction)
                moved.add(box)
            return True

        return False

    def __repr__(self):
        return f"Box({self.x1}/{self.x2}, {self.y})"

    def __hash__(self) -> int:
        return self.gps()

    def __eq__(self, other):
        return self.gps() == other.gps()


def in_bounds(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def move(grid, current, direction):
    x, y = current
    dx, dy = direction
    nx, ny = x + dx, y + dy

    return (nx, ny) if in_bounds(grid, nx, ny) and grid[ny][nx] != "#" else current


def solve(print: Callable, print_output: Callable) -> None:
    lines = open(0).read().splitlines()

    grid_lines = takewhile(lambda line: line != "", lines)
    grid = [[char for c in line for char in TILE_MAP[c]] for line in grid_lines]
    # print("\n".join("".join(line) for line in grid))

    robot = x, y = next(
        (x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "@"
    )

    movements = [c for line in lines[len(grid) + 1 :] for c in line]

    boxes = [
        Box(x, y)
        for x in range(len(grid[0]))
        for y in range(len(grid))
        if grid[y][x] == "["
    ]

    box_grid: dict[tuple[int, int], Box] = {}

    for box in boxes:
        box_grid[box.x1, box.y] = box
        box_grid[box.x2, box.y] = box

    walls = {
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[0]))
        if grid[y][x] == "#"
    }

    for movement in movements:
        grid[y][x] = "."

        direction = DIRECTION_MAP[movement]
        new_robot = nx, ny = move(grid, robot, direction)

        if new_robot in walls or (
            new_robot in box_grid
            and not box_grid[new_robot].attempt_move(grid, walls, box_grid, direction)
        ):
            grid[y][x] = "@"
        else:
            grid[ny][nx] = "@"
            robot = x, y = new_robot

    gps = sum(box.gps() for box in boxes)
    print_output(gps)
