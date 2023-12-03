use std::fs;

fn parse_range(s: &Vec<&str>) -> (u32, u32) {
    let x = s[0].parse::<u32>().expect("Couldn't convert to u32");
    let y = s[1].parse::<u32>().expect("Couldn't convert to u32");
    (x, y)
}

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let mut count = 0;

    for pair in data.lines() {
        let ranges: Vec<&str> = pair.split(",").collect();
        let pair1: Vec<&str> = ranges[0].split("-").collect();
        let pair2: Vec<&str> = ranges[1].split("-").collect();
        let (l1, r1) = parse_range(&pair1);
        let (l2, r2) = parse_range(&pair2);
        if (l1 <= l2 && r1 >= r2) || (l1 >= l2 && r1 <= r2) {
            count += 1;
        }
    }

    println!("{}", count);
}