
use std::io;

fn prime(x: i32) -> i32 
{
    let mut count = 0;
    for i in 1..=x 
    {
        if x % i == 0 
        {
            count += 1;
        }
    }
    if count == 2 
    {
        return 1;
    } else 
    {
        return 0;
    }
}

fn main() 
{
    println!("Enter the limit: ");
    let mut num = String::new();

    io::stdin()
        .read_line(&mut num)
        .expect("Failed to read line");

    let n: i32 = match num.trim().parse() 
    {
        Ok(num) => num,
        Err(_) => 
        {
            println!("Please enter a valid limit!");
            return;
        }
    };

    for i in 2..=n 
    {
        if prime(i) == 1 
        {
            println!("{}", i);
        }
    }
}
