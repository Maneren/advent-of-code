def solve(print, print_output):
    lines = open(0).read().splitlines()

    sum_of_powers = 0

    for line in lines:
        print(line, line.split(": "))
        header, body = line.split(": ")
        _, id = header.split()
        id = int(id)

        required = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        showings = body.split("; ")
        for showing in showings:
            cubes = showing.split(", ")

            for cube in cubes:
                count, color = cube.split()

                count = int(count)

                if count > required[color]:
                    required[color] = count

        power = required["red"] * required["green"] * required["blue"]

        sum_of_powers += power

    print_output(sum_of_powers)
