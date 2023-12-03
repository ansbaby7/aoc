use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from string");
    let lines: Vec<&str> = data.trim().split("\n").collect();

    let mut dir_sizes:HashMap<String, u32> = HashMap::new();
    let mut path = String::new();
   
    let mut i = 0;
    while i < lines.len(){
        let v: Vec<_> = lines[i].split(" ").collect();
        if v[1] == "cd" {
            if v[2] == "/" {
                path = "root".to_string();
            } else if v[2] == ".." {
                let (x, _) = path.rsplit_once("/").unwrap();
                path = x.to_string();
            } else {
                path = format!("{}/{}", path, v[2]);
            }
            i += 1;
        } else if v[1] == "ls" {
            i += 1;
            let mut size = 0;
            while i < lines.len() && lines[i].split(" ").collect::<Vec<_>>()[0] != "$" {
                let (x, _) = lines[i].split_once(" ").unwrap();
                if x != "dir" {
                    let filesize = x.parse::<u32>().unwrap();
                    size += filesize;
                }
                i += 1
            }
            *dir_sizes.entry(path.clone()).or_insert(0) = size;
            if path != "root" {
                let (mut x, _) = path.rsplit_once("/").unwrap();
                loop {
                    *dir_sizes.entry(x.to_string()).or_insert(0) += size;
                    if x == "root" {
                        break;
                    }
                    (x, _) = x.rsplit_once("/").unwrap();
                }   
            }
        }
    }

    let root_size = dir_sizes["root"];
    let free_space = 70000000 - root_size;
    let needed = 30000000;
    let to_free = needed - free_space;

    let mut min = root_size;
    for (_, size) in dir_sizes {
        if size >= to_free && size < min {
            min = size;
        }
    }
    println!("{}", min);    
}

