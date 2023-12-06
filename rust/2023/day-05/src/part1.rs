use itertools::*;
use std::time::Instant;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

fn parse_number_from_iter<'a>(iter: &mut impl Iterator<Item = &'a str>) -> Result<i64, String> {
    iter.next()
        .ok_or("No number")?
        .parse::<i64>()
        .map_err(|e| e.to_string())
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let mut lines = input.lines();

    let (_header, seeds) = lines
        .next()
        .ok_or("No header")?
        .split_once("seeds: ")
        .ok_or("No seeds")?;

    let mut seeds: Vec<_> = seeds
        .split(' ')
        .map(|s| s.parse::<i64>().map_err(|e| e.to_string()))
        .try_collect()?;

    let _ = lines.next(); // skip line after seeds

    while lines.next().is_some() {
        // skips the header line

        let mut mapping = vec![];

        // load the mappings block
        while let Some(line) = lines.next() {
            if line.is_empty() {
                break;
            }

            // parse the line
            let mut splitted = line.split(' ');
            let destination = parse_number_from_iter(&mut splitted)?;
            let source = parse_number_from_iter(&mut splitted)?;
            let length = parse_number_from_iter(&mut splitted)?;

            mapping.push((source, destination - source, length));
        }

        mapping.sort_unstable_by_key(|a| a.0);
        seeds.sort_unstable();

        // if current seed isn't in range, no future one can be as well
        // since they are sorted
        let mut used_up = 0;

        'outer: for seed in &mut seeds {
            for (src_start, offset, length) in &mapping[used_up..] {
                if src_start <= seed && *seed < src_start + length {
                    *seed += offset;
                    continue 'outer;
                }
                used_up += 1;
            }
        }
    }

    Ok(seeds.into_iter().min().ok_or("No seed left at the end")?)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";
        let result = solve(input)?.to_string();
        assert_eq!("35", result);
        Ok(())
    }
}

