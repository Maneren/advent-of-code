def solve(print, print_output):
    lines = open(0).read().splitlines()

    sum = 0

    for line in lines:
        for char in line:
            if char.isdigit():
                first = int(char)
                break

        for char in reversed(line):
            if char.isdigit():
                last = int(char)
                break

        sum += int(f"{first}{last}")

    print_output(sum)
