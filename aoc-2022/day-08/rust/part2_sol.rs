use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let grid: Vec<_> = data.split("\n").collect();
    let l = grid.len();

    let mut max_score = 0;
    for i in 1..l-1 {
        for j in 1..l-1 {
            let left = grid[i][0..j].chars().rev().collect::<Vec<_>>();
            let right = grid[i][j+1..l].chars().collect::<Vec<_>>();
            let mut up = vec!['0'; i];
            for k in 1..i+1 {
                up[k-1] = grid[i-k][j..j+1].chars().nth(0).unwrap(); 
            }
            let mut down = vec!['0'; l-i-1];
            for k in 1..l-i {
                down[k-1] = grid[i+k][j..j+1].chars().nth(0).unwrap();
            }

            let mut score = 1;
            for side in [left, right, up, down] {
                let mut count = 0;
                for height in side {
                    count += 1;
                    if height >= grid[i][j..j+1].chars().nth(0).unwrap() {
                        break;
                    }
                }
                score *= count;
            }
            if score > max_score {
                max_score = score;
            }
        }
    }
    println!("{}", max_score);
}