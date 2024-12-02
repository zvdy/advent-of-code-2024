use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn is_safe_report(report: &str) -> bool {
    let levels: Vec<i32> = report.split_whitespace()
                                 .map(|s| s.parse().unwrap())
                                 .collect();
    let mut increasing = true;
    let mut decreasing = true;

    for i in 0..levels.len() - 1 {
        let diff = levels[i + 1] - levels[i];
        if diff < 1 || diff > 3 {
            increasing = false;
        }
        if diff > -1 || diff < -3 {
            decreasing = false;
        }
    }

    increasing || decreasing
}

fn can_be_safe_with_removal(levels: &[i32]) -> bool {
    for i in 0..levels.len() {
        let mut modified_levels = levels.to_vec();
        modified_levels.remove(i);
        if is_safe_report(&join_levels(&modified_levels)) {
            return true;
        }
    }
    false
}

fn count_safe_reports_part1(data: &str) -> usize {
    data.lines()
        .filter(|&report| is_safe_report(report))
        .count()
}

fn count_safe_reports_part2(data: &str) -> usize {
    data.lines()
        .filter(|&report| {
            let levels: Vec<i32> = report.split_whitespace()
                                         .map(|s| s.parse().unwrap())
                                         .collect();
            is_safe_report(report) || can_be_safe_with_removal(&levels)
        })
        .count()
}

fn join_levels(levels: &[i32]) -> String {
    levels.iter()
          .map(|&level| level.to_string())
          .collect::<Vec<String>>()
          .join(" ")
}

fn main() {
    let path = "input.txt";
    let input_data = read_lines(path).expect("Could not read file");

    let part1_safe_count = count_safe_reports_part1(&input_data);
    let part2_safe_count = count_safe_reports_part2(&input_data);

    println!("Part 1: {} safe reports", part1_safe_count);
    println!("Part 2: {} safe reports", part2_safe_count);
}

// Helper function to read lines from a file
fn read_lines<P>(filename: P) -> io::Result<String>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let buf = io::BufReader::new(file);
    let mut contents = String::new();
    for line in buf.lines() {
        contents.push_str(&line?);
        contents.push('\n');
    }
    Ok(contents)
}