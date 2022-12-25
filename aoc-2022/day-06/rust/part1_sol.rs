use std::fs;
use std::collections::HashSet;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    for i in 4..data.len() {
        let mut set = HashSet::new();
        for c in data[i-4..i].chars() {
            set.insert(c);
        }
        if set.len() == 4 {
            println!("{}", i);
            break;
        }
    }
}