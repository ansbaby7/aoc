use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read file");
    let mut calories: i32 = 0;
    let mut max1 = 0;
    let mut max2 = 0;
    let mut max3 = 0;
    for val in data.lines() {
        if val == "" {
            if calories > max1 {
                max3 = max2;
                max2 = max1;
                max1 = calories;
            } else if calories > max2 {
                max3 = max2;
                max2 = calories;
            } else if calories > max3 {
                max3 = calories;
            }
            calories = 0;
        } else {
            calories += val.parse::<i32>().expect("Couldn't convert to i32");
        }
    }

    println!("{}", max1 + max2 + max3);
}