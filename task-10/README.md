



This was probably a task that I thought was going to be really hard but ended up being way easier than I thought. When I followed the documentation for this task everything kinda made sense and it was really easy to follow through till the end. I basically downloaded all the requirements and created a config.toml in a .cargo directory. I then added the following code to it:

```toml
[unstable]
build-std-features = ["compiler-builtins-mem"]
build-std = ["core", "compiler_builtins"]

[build]
target = "x86_64-rusk.json"

[dependencies]
bootimage = "0.10.15"

[target.'cfg(target_os = "none")']
runner = "bootimage runner"
```

I resolved some syntax errors in the main.rs that showed up in the terminal when I ran the file. 
In vga-buffer.rs I interchanged the values Black and Red in the enumeration. In interrupts.rs:
```rust
pub enum Color {
    Black = 0,
    Blue = 1,
    Green = 2,
    Cyan = 3,
    Red = 4,
    Magenta = 5,
    Brown = 6,
    LightGray = 7,
    DarkGray = 8,
    LightBlue = 9,
    LightGreen = 10,
    LightCyan = 11,
    LightRed = 12,
    Pink = 13,
    Yellow = 14,
    White = 15,
}
```
 I basically changed the loop to read the characters in the right order rather than the reverse order in which it previously did:

```rust
fn add_character(chars: &mut [Option<char>; ARRAY_SIZE], character: char) -> Result<(), &'static str> {
    if chars[0].is_none() {
        // The array is full, remove the last character
        chars[ARRAY_SIZE - 1] = None;
    }

    // Find the first available index (None) and insert the new character
    unsafe {
        for i in 0..=ARRAY_SIZE {
            if chars[i].is_none() {
                chars[i] = Some(character);
                return Ok(());
            }
        }
    }

    Err("Left shift failed. Cannot add more characters.")
}
```