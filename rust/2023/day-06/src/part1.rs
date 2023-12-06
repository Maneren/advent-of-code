use std::time::Instant;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

fn parse_line(line: &str) -> Result<impl Iterator<Item = Result<i32, String>> + '_, String> {
    let (_header, numbers) = line.split_once(':').ok_or("No colon in the line")?;
    Ok(numbers
        .trim()
        .split_whitespace()
        .map(|s| s.parse::<i32>().map_err(|e| e.to_string())))
}

fn solve_reduced_quadratic(b: i32, c: i32) -> f32 {
    let discriminant = (b.pow(2) - 4 * c) as f32;
    assert!(discriminant >= 0.0, "No solution");
    (-b as f32 - discriminant.sqrt()) / 2.0
}

fn next_larger_integer(x: f32) -> i32 {
    let ceiled = x.ceil();
    if (ceiled - x) < f32::EPSILON {
        ceiled as i32 + 1
    } else {
        ceiled as i32
    }
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let mut lines = input.lines();
    let times_line = lines.next().ok_or("No lines in input")?;
    let times = parse_line(times_line)?;

    let distances_line = lines.next().ok_or("No lines in input")?;
    let distances = parse_line(distances_line)?;

    let mut product = 1;

    for (time, distance) in times.zip(distances) {
        let time = time?;
        let distance = distance?;
        let lower_limit = solve_reduced_quadratic(-time, distance);
        let lower_limit = next_larger_integer(lower_limit);
        let time_window = time - lower_limit * 2 + 1;
        product *= time_window;
    }

    Ok(product)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "Time:      7  15   30
Distance:  9  40  200";
        let result = solve(input)?.to_string();
        assert_eq!("288", result);
        Ok(())
    }
}
