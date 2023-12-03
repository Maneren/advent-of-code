use crate::custom_error::AocError;

#[tracing::instrument]
pub fn process(input: &str) -> miette::Result<String, AocError> {
    let find_first_digit =
        |iter: &mut dyn Iterator<Item = char>| iter.filter_map(|c| c.to_digit(10)).next();

    Ok(input
        .lines()
        .map(|line| {
            // find first digit in the line
            let first =
                find_first_digit(&mut line.chars()).expect("line contains at least one digit");

            // if there's no last, it's the same as the first
            let last = find_first_digit(&mut line.chars().rev())
                .expect("line contains at least one digit");

            first * 10 + last
        })
        .sum::<u32>()
        .to_string())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> miette::Result<()> {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
        assert_eq!("142", process(input)?);
        Ok(())
    }
}
