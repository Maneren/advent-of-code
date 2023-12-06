def split_to_ints(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def solve(print, print_output):
    lines = open(0).read().splitlines()

    header, seed_ranges = lines[0].split(": ")

    assert header == "seeds"

    seed_ranges = split_to_ints(seed_ranges)

    starts = seed_ranges[::2]
    lenghts = seed_ranges[1::2]

    seed_ranges = list(zip(starts, lenghts))

    i = 1
    while i < len(lines):
        i += 1
        mappings = []
        header, _ = lines[i].split(" ")
        source, dest = header.split("-to-")

        i += 1
        while i < len(lines) and (line := lines[i]):
            dest_start, src_start, length = split_to_ints(line)
            mappings.append((src_start, dest_start - src_start, length))
            i += 1

        mappings.sort(key=lambda x: x[0])

        seed_ranges.sort()

        # try merging neighboring ranges
        j = 0
        while j < len(seed_ranges) - 1:
            a = seed_ranges[j]
            b = seed_ranges[j + 1]

            if a[0] + a[1] == b[0]:
                seed_ranges[j] = (a[0], a[1] + b[1])
                seed_ranges.pop(j + 1)
                print("merging")
            else:
                j += 1

        print(seed_ranges)
        print(mappings)

        new_ranges = []

        j = 0
        while j < len(seed_ranges):
            print(f"{j} ouf of {len(seed_ranges)}")
            start, length = seed_ranges[j]
            end = start + length - 1

            for src_start, offset, mapping_length in mappings:
                src_end = src_start + mapping_length - 1

                if not (src_start <= start <= src_end):
                    continue

                output_start = start + offset

                if end > src_end:
                    remaining_length = end - (src_end - 1) - 1
                    seed_ranges.append((src_end + 1, remaining_length))
                    length = length - remaining_length

                new_ranges.append((output_start, length))
                break

            else:
                new_ranges.append((start, length))

            j += 1

        seed_ranges = new_ranges

    print(seed_ranges)

    print_output(min(seed_ranges))


if __name__ == "__main__":
    solve(print, print)
