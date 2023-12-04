use std::time::Instant;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let mut line_counts = vec![1];
    let total = input
        .lines()
        .enumerate()
        .map(|(i, line)| {
            let (_, numbers) = line.split_once(": ").unwrap();
            let (winning, my) = numbers.split_once(" | ").unwrap();

            let mut buffer = [0; 100];

            winning
                .split_ascii_whitespace()
                .map(|number| number.parse::<usize>().unwrap())
                .for_each(|number| {
                    buffer[number] = 1;
                });

            let wins = my
                .split_ascii_whitespace()
                .map(|number| number.parse::<usize>().unwrap())
                .filter(|&number| buffer[number] == 1)
                .count();

            if i + wins >= line_counts.len() {
                line_counts.resize(i + wins + 1, 1);
            }

            let current_count = line_counts[i];

            for j in 0..wins {
                line_counts[i + j + 1] += current_count;
            }

            current_count
        })
        .sum::<usize>();

    Ok(total)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";
        let result = solve(input)?.to_string();
        assert_eq!("30", result);
        Ok(())
    }
}
