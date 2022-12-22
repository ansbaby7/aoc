use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let mut sum = 0;
    for rucksack in data.lines() {
        let l = rucksack.len();
        let left = &rucksack[0..l/2];
        let right = &rucksack[l/2..l];
        for item in left.chars() {
            let v = right.chars().collect::<Vec<char>>();
            if v.contains(&item) {
                let ord = item as u32;
                if ord > 97 {
                    sum += ord - 96;
                } else {
                    sum += ord - 64 + 26;
                }
                break;
            }
        }
    }

    println!("{}", sum);
}