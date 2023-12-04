use std::time::Instant;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

const MAX_RED: i32 = 12;
const MAX_GREEN: i32 = 13;
const MAX_BLUE: i32 = 14;

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let sum = input
        .lines()
        .filter_map(|line| {
            let (header, rest) = line.split_once(": ")?;

            let impossible = rest.split("; ").any(|showing| {
                showing.split(", ").any(|cube| {
                    let (amount, color) = cube.split_once(' ').unwrap();
                    let amount = amount.parse::<i32>().unwrap();

                    match color {
                        "red" => amount > MAX_RED,
                        "blue" => amount > MAX_BLUE,
                        "green" => amount > MAX_GREEN,
                        _ => unreachable!(),
                    }
                })
            });

            if impossible {
                None
            } else {
                let (_, id) = header.split_once(' ')?;
                id.parse::<i32>().ok()
            }
        })
        .sum::<i32>();

    Ok(sum)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let result = solve(input)?.to_string();
        assert_eq!("8", result);
        Ok(())
    }
}
