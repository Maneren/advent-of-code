from math import ceil, floor


def solve_quadratic(a: int, b: int, c: int) -> list[int] | None:
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None

    return [
        (-b - discriminant**0.5) / (2 * a),
        (-b + discriminant**0.5) / (2 * a),
    ]


def next_larger_integer(x: float) -> int:
    ceiled = ceil(x)
    return ceiled if ceiled != x else ceiled + 1


def next_smaller_integer(x: float) -> int:
    floored = floor(x)
    return floored if floored != x else floored - 1


def solve(print, print_output):
    lines = open(0).read().splitlines()

    lines_without_headers = (line.split(":")[1] for line in lines)

    lines = map(str.split, map(str.strip, lines_without_headers))

    print(lines)

    races = zip(*lines)

    product = 1

    for time, record_distance in races:
        time = int(time)
        record_distance = int(record_distance)
        print(time, record_distance)
        min_range_at_start = solve_quadratic(1, -time, record_distance)

        assert min_range_at_start is not None

        print(min_range_at_start)

        min_time, max_time = min_range_at_start

        min_time = next_larger_integer(min_time)
        max_time = next_smaller_integer(max_time)

        time_window = max_time - min_time + 1  # include both start and end

        print(min_time, max_time, time_window)

        product *= time_window

    print_output(product)
