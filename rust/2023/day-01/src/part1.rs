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
    fn find_first_digit(mut iter: impl Iterator<Item = char>) -> Option<u32> {
        iter.find_map(|c| c.to_digit(10))
    }

    let sum = input
        .lines()
        .map(|line| {
            // find the first digit in the line
            let first = find_first_digit(line.chars()).expect("line contains at least one digit");

            // if there's no last, it's the same as the first
            let last =
                find_first_digit(line.chars().rev()).expect("line contains at least one digit");

            first * 10 + last
        })
        .sum::<u32>();

    Ok(sum)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
        let result = solve(input)?.to_string();
        assert_eq!("142", result);
        Ok(())
    }
}
