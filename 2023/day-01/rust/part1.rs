use std::fs;


fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    // let data = fs::read_to_string("../sample.txt").expect("Couldn't read from file");
    let mut ans = 0;
    let digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for line in data.lines() {
        // let v: Vec<char> = line.chars().collect();
        let ch1 = line.chars().find(|&ch| ch > '0' && ch <= '9').unwrap();
        let d1 = ch1.to_digit(10).unwrap();
        let ch2 = line.chars().rfind(|&ch| ch > '0' && ch <= '9').unwrap();
        let d2 = ch2.to_digit(10).unwrap();
        ans += d1 * 10 + d2;
        // println!("{d1} {d2}");
    }
    println!("{ans}")
}