use std::fs;
use std::collections::HashSet;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    for i in 14..data.len() {
        let mut set = HashSet::new();
        for c in data[i-14..i].chars() {
            set.insert(c);
        }
        if set.len() == 14 {
            println!("{}", i);
            break;
        }
    }
}