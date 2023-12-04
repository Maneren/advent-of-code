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
    todo!("Haven't built part 1 yet");

    Ok(0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        todo!("Haven't built test yet");
        let input = "";
        let result = solve(input)?.to_string();
        assert_eq!("", result);
        Ok(())
    }
}
