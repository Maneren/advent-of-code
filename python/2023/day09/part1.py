def differentiate(values: list[int]) -> list[int]:
    return [b - a for a, b in zip(values, values[1:])]


def solve(print, print_output):
    lines = open(0).read().splitlines()

    total = 0

    for line in lines:
        values = list(map(int, line.split()))

        derivatives = [values]

        while any(x != 0 for x in derivatives[-1]):
            derivatives.append(differentiate(derivatives[-1]))

        for i in reversed(range(len(derivatives) - 1)):
            values = derivatives[i]
            previous = derivatives[i + 1]
            new_value = values[-1] + previous[-1]

            values.append(new_value)

        total += derivatives[0][-1]

    print_output(total)
