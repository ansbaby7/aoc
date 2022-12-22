use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let mut sum = 0;
    let rucksacks: Vec<&str> = data.lines().collect();
    let l = rucksacks.len();
    for i in (0..l).step_by(3) {
        for item in rucksacks[i].chars() {
            let v = rucksacks[i+1].chars().collect::<Vec<char>>();
            let w = rucksacks[i+2].chars().collect::<Vec<char>>();
            if v.contains(&item) && w.contains(&item) {
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