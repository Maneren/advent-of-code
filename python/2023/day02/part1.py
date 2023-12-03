max_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def solve(print, print_output):
    lines = open(0).read().splitlines()

    sum_of_possible = 0

    for line in lines:
        print(line, line.split(": "))
        header, body = line.split(": ")
        _, id = header.split()
        id = int(id)

        impossible = False

        showings = body.split("; ")
        for showing in showings:
            cubes = showing.split(", ")

            for cube in cubes:
                count, color = cube.split()

                count = int(count)

                if count > max_counts[color]:
                    impossible = True
                    break

        if not impossible:
            sum_of_possible += id

    print_output(sum_of_possible)
