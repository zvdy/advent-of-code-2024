use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn calculate_total_distance(mut left_list: Vec<i32>, mut right_list: Vec<i32>) -> i32 {
    // Sort both lists
    left_list.sort();
    right_list.sort();

    // Calculate the total distance
    let mut total_distance = 0;
    for (left, right) in left_list.iter().zip(right_list.iter()) {
        total_distance += (left - right).abs();
    }

    total_distance
}

fn calculate_similarity_score(left_list: Vec<i32>, right_list: Vec<i32>) -> i32 {
    // Count the occurrences of each number in the right list
    let mut right_count = HashMap::new();
    for num in right_list {
        *right_count.entry(num).or_insert(0) += 1;
    }

    // Calculate the similarity score
    let mut similarity_score = 0;
    for num in left_list {
        if let Some(count) = right_count.get(&num) {
            similarity_score += num * count;
        }
    }

    similarity_score
}

fn read_input_file(file_path: &str) -> io::Result<(Vec<i32>, Vec<i32>)> {
    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split_whitespace().collect();
        let left = parts[0].parse::<i32>().unwrap();
        let right = parts[1].parse::<i32>().unwrap();
        left_list.push(left);
        right_list.push(right);
    }

    Ok((left_list, right_list))
}

fn main() {
    // Read the input file
    let (left_list, right_list) = match read_input_file("input.txt") {
        Ok((left, right)) => (left, right),
        Err(err) => {
            eprintln!("Error reading input file: {}", err);
            return;
        }
    };

    // Calculate the total distance
    let total_distance = calculate_total_distance(left_list.clone(), right_list.clone());
    println!("Total distance: {}", total_distance);

    // Calculate the similarity score
    let similarity_score = calculate_similarity_score(left_list, right_list);
    println!("Similarity score: {}", similarity_score);
}