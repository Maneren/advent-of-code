def solve(print, print_output):
    lines = open(0).read().splitlines()

    total = 0

    for line in lines:
        buffer = [0] * 100
        _, numbers = line.split(": ")
        winning, my = (x.split() for x in numbers.split(" | "))

        line_total = 0

        for number in winning:
            buffer[int(number)] = 1

        for number in my:
            if buffer[int(number)] == 1:
                if not line_total:
                    line_total = 1
                else:
                    line_total *= 2

        print(line_total)
        total += line_total

    print(total)
    print_output(total)
