def process_scratchcard(lines: list[str], current: int) -> int:
    buffer = [0] * 100
    _, numbers = lines[current].split(": ")
    winning, my = (x.split() for x in numbers.split(" | "))

    for number in winning:
        buffer[int(number)] = 1

    return sum(buffer[int(number)] == 1 for number in my)


def solve(print, print_output):
    lines = open(0).read().splitlines()

    total = 0

    card_counts = [1] * len(lines)

    for i, card in enumerate(lines):
        print(f"Processing {card_counts[i]} card(s) {i}")
        total += card_counts[i]
        wins = process_scratchcard(lines, i)

        for j in range(wins):
            card_counts[i + j + 1] += card_counts[i]

        print(card_counts)

    print_output(total)
