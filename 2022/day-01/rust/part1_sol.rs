use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read file");
    let mut calories: i32 = 0;
    let mut max = 0;
    for val in data.lines() {
        if val == "" {
            if calories > max {
                max = calories;
            }
            calories = 0;
        } else {
            calories += val.parse::<i32>().expect("Couldn't convert to i32");
        }
    }

    println!("{}", max);
}