from math import ceil, floor


def solve_quadratic(a: int, b: int, c: int) -> list[int] | None:
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None

    return [
        (-b + discriminant**0.5) / (2 * a),
        (-b - discriminant**0.5) / (2 * a),
    ]


def next_larger_integer(x: float) -> int:
    ceiled = ceil(x)
    if ceiled == x:
        return ceiled + 1
    else:
        return ceiled


def next_smaller_integer(x: float) -> int:
    floored = floor(x)
    if floored == x:
        return floored - 1
    else:
        return floored


def solve(print, print_output):
    lines = open(0).read().splitlines()

    time_line, distance_line = lines

    time = int(time_line.split(":")[1].replace(" ", ""))
    record_distance = int(distance_line.split(":")[1].replace(" ", ""))

    print(time, record_distance)

    min_range_at_start = solve_quadratic(1, -time, record_distance)

    min_time, max_time = (
        next_larger_integer(min(min_range_at_start)),
        next_smaller_integer(max(min_range_at_start)),
    )

    time_window = max_time - min_time + 1  # include both start and end

    print_output(time_window)
