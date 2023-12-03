use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let mut score = 0;
    for line in data.lines() {
        let s: Vec<&str> = line.split(" ").collect();
        if s[0] == "A" {
            if s[1] == "Y" {
                score += 3 + 1;
            } else if s[1] == "Z" {
                score += 6 + 2;
            } else {
                score += 0 + 3;
            }
        } else if s[0] == "B" {
            if s[1] == "Y" {
                score += 3 + 2;
            } else if s[1] == "Z" {
                score += 6 + 3;
            } else {
                score += 0 + 1;
            }
        } else {
            if s[1] == "Y" {
                score += 3 + 3;
            } else if s[1] == "Z" {
                score += 6 + 1;
            } else {
                score += 0 + 2;
            }
        }
    }

    println!("{}", score);
}