import re

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solve(print, print_output):
    lines = open(0).read().splitlines()
    sum = 0

    for line in lines:
        from_beggining = re.findall(
            r"\d|one|two|three|four|five|six|seven|eight|nine", line
        )
        from_end = re.findall(
            r".*(\d|one|two|three|four|five|six|seven|eight|nine)", line
        )
        print(line, from_beggining)

        first = from_beggining[0]
        last = from_end[0]

        first = numbers[first] if first in numbers else first
        last = numbers[last] if last in numbers else last

        number = int(f"{first}{last}")

        print(number)

        sum += number

    print_output(sum)
