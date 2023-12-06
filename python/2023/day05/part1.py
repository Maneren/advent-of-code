def split_to_ints(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def solve(print, print_output):
    lines = open(0).read().splitlines()

    header, seeds = lines[0].split(": ")

    assert header == "seeds"

    seeds = split_to_ints(seeds)

    i = 1
    while i < len(lines):
        i += 1
        mapping = []
        header, _ = lines[i].split(" ")
        source, dest = header.split("-to-")

        i += 1
        while i < len(lines) and (line := lines[i]):
            dest_start, src_start, length = split_to_ints(line)
            mapping.append((src_start, dest_start, length))
            i += 1

        mapping.sort(key=lambda x: x[0])

        print(mapping)

        seeds.sort()

        for j, seed in enumerate(seeds):
            for src_start, dest_start, length in mapping:
                if src_start <= seed < src_start + length:
                    print(f"{seed} -> {dest_start + seed - src_start}")
                    seeds[j] = dest_start + seed - src_start
                    break
            else:
                print(f"{seed} -> {seed}")

    print_output(min(seeds))
