use std::time::Instant;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

fn parse_line(line: &str) -> Result<usize, String> {
    let (_header, numbers) = line.split_once(':').ok_or("No colon in the line")?;

    let number_string = numbers.replace(' ', "");

    number_string.parse::<usize>().map_err(|e| e.to_string())
}

fn solve_reduced_quadratic(b: f32, c: f32) -> f32 {
    let discriminant = b.powi(2) - 4.0 * c;
    assert!(discriminant >= 0.0, "No solution");
    (-b - discriminant.sqrt()) / 2.0
}

fn next_larger_integer(x: f32) -> usize {
    let ceiled = x.ceil();
    if (ceiled - x) < f32::EPSILON {
        ceiled as usize + 1
    } else {
        ceiled as usize
    }
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let mut lines = input.lines();
    let times_line = lines.next().ok_or("No lines in input")?;
    let time = parse_line(times_line)?;

    let distances_line = lines.next().ok_or("No lines in input")?;
    let distance = parse_line(distances_line)?;

    let lower_limit = solve_reduced_quadratic(-(time as f32), distance as f32);
    let lower_limit = next_larger_integer(lower_limit);
    let time_window = time - lower_limit * 2 + 1;

    Ok(time_window)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "Time:      7  15   30
Distance:  9  40  200";
        let result = solve(input)?.to_string();
        assert_eq!("71503", result);
        Ok(())
    }
}
