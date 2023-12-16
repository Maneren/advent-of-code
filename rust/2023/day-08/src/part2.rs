use std::{convert::identity, ops::Index, time::Instant};

use rustc_hash::FxHashMap;

#[allow(dead_code)]
fn main() -> Result<(), String> {
    let start = Instant::now();
    let result = solve(include_str!("../input.txt")).map_err(|e| e.to_string())?;
    let elapsed = start.elapsed();
    println!("'{}' in {elapsed:?}", result.to_string());
    Ok(())
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Direction {
    Right = 0,
    Left = 1,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct Mapping<'a> {
    left: &'a str,
    right: &'a str,
}

impl<'a> Index<Direction> for Mapping<'a> {
    type Output = &'a str;
    fn index(&self, index: Direction) -> &Self::Output {
        match index {
            Direction::Right => &self.right,
            Direction::Left => &self.left,
        }
    }
}

pub fn solve(input: &str) -> Result<impl ToString, String> {
    let lines = input.lines().map(|line| line.trim()).collect::<Vec<&str>>();

    let directions = lines[0]
        .chars()
        .map(|c| match c {
            'R' => Direction::Right,
            'L' => Direction::Left,
            _ => unreachable!(),
        })
        .cycle();

    let mut starting = vec![];

    let mappings = lines[2..]
        .into_iter()
        .map(|line| {
            let (from, to) = line
                .split_once(" = ")
                .ok_or_else(|| format!("Invalid mapping line: {line}"))?;

            let (left, right) = to[1..to.len() - 1]
                .split_once(", ")
                .ok_or_else(|| format!("Invalid mapping: {to}"))?;

            let to = Mapping { left, right };

            if from.ends_with('A') {
                starting.push(from);
            }

            Ok((from, to))
        })
        .collect::<Result<FxHashMap<_, _>, String>>()?;

    let mut loops = vec![None; starting.len()];

    for (i, direction) in directions.into_iter().enumerate() {
        if loops.iter().all(Option::is_some) {
            break;
        }

        loops
            .iter_mut()
            .zip(starting.iter_mut())
            .filter(|(loop_, _)| loop_.is_none())
            .for_each(|(loop_, starting)| {
                *starting = mappings[starting][direction];

                if starting.ends_with('Z') {
                    *loop_ = Some(i + 1);
                }
            })
    }

    let steps = loops
        .into_iter()
        .filter_map(identity)
        .fold(1, num::integer::lcm);

    Ok(steps)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_process() -> Result<(), String> {
        let input = "LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)";
        let result = solve(input)?.to_string();
        assert_eq!("6", result);
        Ok(())
    }
}

