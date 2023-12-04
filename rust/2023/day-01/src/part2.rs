#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = std::time::Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let output = input
        .lines()
        .map(|line| {
            let first = (0..line.len())
                .find_map(|i| match &line.as_bytes()[i..] {
                    [b'1', ..] | [b'o', b'n', b'e', ..] => Some(10),
                    [b'2', ..] | [b't', b'w', b'o', ..] => Some(20),
                    [b'3', ..] | [b't', b'h', b'r', b'e', b'e', ..] => Some(30),
                    [b'4', ..] | [b'f', b'o', b'u', b'r', ..] => Some(40),
                    [b'5', ..] | [b'f', b'i', b'v', b'e', ..] => Some(50),
                    [b'6', ..] | [b's', b'i', b'x', ..] => Some(60),
                    [b'7', ..] | [b's', b'e', b'v', b'e', b'n', ..] => Some(70),
                    [b'8', ..] | [b'e', b'i', b'g', b'h', b't', ..] => Some(80),
                    [b'9', ..] | [b'n', b'i', b'n', b'e', ..] => Some(90),
                    _ => None,
                })
                .expect("line contains at least one digit");

            let last = (0..line.len())
                .rev()
                .find_map(|i| match &line.as_bytes()[..=i] {
                    [.., b'1'] | [.., b'o', b'n', b'e'] => Some(1),
                    [.., b'2'] | [.., b't', b'w', b'o'] => Some(2),
                    [.., b'3'] | [.., b't', b'h', b'r', b'e', b'e'] => Some(3),
                    [.., b'4'] | [.., b'f', b'o', b'u', b'r'] => Some(4),
                    [.., b'5'] | [.., b'f', b'i', b'v', b'e'] => Some(5),
                    [.., b'6'] | [.., b's', b'i', b'x'] => Some(6),
                    [.., b'7'] | [.., b's', b'e', b'v', b'e', b'n'] => Some(7),
                    [.., b'8'] | [.., b'e', b'i', b'g', b'h', b't'] => Some(8),
                    [.., b'9'] | [.., b'n', b'i', b'n', b'e'] => Some(9),
                    _ => None,
                })
                .expect("line contains at least one digit");

            first + last
        })
        .sum::<u32>();

    Ok(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";
        let result = solve(input)?.to_string();
        assert_eq!("281", result);
        Ok(())
    }
}
