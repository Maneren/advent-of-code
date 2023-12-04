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
    let sum = input
        .lines()
        .map(|line| {
            let (_, rest) = line.split_once(": ").unwrap();

            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;

            rest.split("; ").for_each(|showing| {
                showing.split(", ").for_each(|cube| {
                    let (amount, color) = cube.split_once(' ').unwrap();
                    let amount = amount.parse::<i32>().unwrap();

                    match color {
                        "red" => {
                            red = red.max(amount);
                        }
                        "green" => {
                            green = green.max(amount);
                        }
                        "blue" => {
                            blue = blue.max(amount);
                        }
                        _ => unreachable!(),
                    }
                });
            });

            red * green * blue
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
        assert_eq!("2286", result);
        Ok(())
    }
}
