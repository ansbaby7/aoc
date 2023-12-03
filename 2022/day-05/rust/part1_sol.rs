use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let (starting_stacks, mut rearrangement_steps) = data.split_once("\n\n").unwrap();
    // println!("{} {}", starting_stacks, rearrangement_steps);

    let stack_rows: Vec<&str> = starting_stacks.split("\n").collect();
    let stack_numbers_row = stack_rows.last().unwrap();

    let num_stacks = stack_numbers_row.split(" ").filter(|x| x.parse::<u32>().is_ok()).count();
    let num_stacks = num_stacks as u32;

    let mut stacks: Vec<String> = Vec::new();
    
    for _ in 0..num_stacks {
        stacks.push(String::new());
    }

    for i in (0..stack_rows.len()-1).rev() {
        for j in (1..stack_rows[i].len()).step_by(4) {
            stacks[j/4] += &stack_rows[i][j..j+1];
        }
    }

    stacks = stacks.iter().map(|x| x.trim_end().to_string()).collect();

    // println!("{:?}", stacks);    // stacks before rearrangement

    rearrangement_steps = rearrangement_steps.trim_end();

    for step in rearrangement_steps.split("\n") {
        let numbers = step.split(" ").filter(|x| x.parse::<u32>().is_ok());
        let numbers: Vec<u32> = numbers.map(|x| x.parse::<u32>().unwrap()).collect();
        let (num_items, from, to) = (numbers[0] as usize, numbers[1] as usize - 1, numbers[2] as usize - 1);

        // for _ in 0..num_items {
        //     let ch = stacks[from].pop().unwrap();
        //     stacks[to].push(ch);
        // }

        let l = stacks[from].len();
        let mut crates = stacks[from].split_off(l-num_items);
        crates = crates.chars().rev().collect();
        stacks[to] += &crates;    
    }

    for stack in &stacks {
        print!("{}", stack.chars().last().unwrap());
    }

}