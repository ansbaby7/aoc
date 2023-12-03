use std::fs;

fn main() {
    let data = fs::read_to_string("../input.txt").expect("Couldn't read from file");
    let grid: Vec<_> = data.split("\n").collect();
    let l = grid.len();
    let mut visible = vec![vec![-1; l]; l];
    let mut count = 0;
    
    for k in 0..l {
        let (mut left_max, mut right_max) = (-1, -1);
        let (mut i, mut j) = (0, l-1);
        while i < l {
            let mut val = grid[k][i..i+1].parse::<i32>().unwrap();
            if val > left_max {
                left_max = val;
                if visible[k][i] == -1 {
                    count += 1;
                    visible[k][i] = val;
                }
            }
            val = grid[k][j..j+1].parse::<i32>().unwrap();
            if val > right_max {
                right_max = val;
                if visible[k][j] == -1 {
                    count += 1;
                    visible[k][j] = val;
                }
            }
            i += 1;
            if j > 0 {  // check to avoid runtime error 'attempt to subtract with overflow'
                j -= 1;
            }
        }
    }

    for k in 0..l {
        let (mut up_max, mut down_max) = (-1, -1);
        let (mut i, mut j) = (0, l-1);
        while i < l {
            let mut val = grid[i][k..k+1].parse::<i32>().unwrap();
            if val > up_max {
                up_max = val;
                    if visible[i][k] == -1 {
                        count += 1;
                        visible[i][k] = val;
                    }
                }
                val = grid[j][k..k+1].parse::<i32>().unwrap();
                if val > down_max {
                    down_max = val;
                    if visible[j][k] == -1 {
                        count += 1;
                        visible[j][k] = val;
                    }
                }
                i += 1;
                if j > 0 {  // check to avoid runtime error 'attempt to subtract with overflow'
                    j -= 1;
                }
            }
        }

    // println!("{:?}", visible);
    println!("{}", count);
}