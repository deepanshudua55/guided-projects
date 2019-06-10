# Introduction to C - Day 1

## Why learn C?

- C is still used extensively today
  - Operating Systems
  - Embedded Systems
- Many programming languages are written in C
  - Python, PHP, Ruby
- Manual memory management gives you a better understanding of how things like the register, stack, and heap memory work.
- C produces more efficient programs than many higher-level languages

## Memory

- Memory is like a big array of numbers, at any given index, you can read the value at that index, or store a value.
- These terms all mean the same thing:
  - index into the memory array
  - memory location
  - memory address
  - pointer
- Memory addresses are numbers, just like array indices
- You can the memory address of any variable by using the address-of-operator `&`
- You can get the value stored at any memory address using the dereference operator `*`
