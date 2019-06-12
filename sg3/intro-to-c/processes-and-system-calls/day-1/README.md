# Processes and System Calls - Day 1

## Memory Review

### Stack

- LIFO - Last in first out
  - The stack grows and shrinks as functions push and pop local variables
- It's managed by the CPU
- It has size limits.
- Stack variables are temporary
  - They only exist while the function that created them is running
- Variables on the stack can't be resized.
- Accessing the stack is fast.

### Heap

- Variables stored on the heap can be accessed globally.
- No limit in size.
- It has be managed manually
  - We use `malloc` to store variables on the heap
  - We use `free` to remove things from the heap
  - If we don't have 1 `free` for every `malloc` call then we'll get a memory leak.
- We can use `realloc` to resize variables on the heap.
- Accessing the heap is slower.

### Summary

- The stack is fast, automated, and temporary.
- The heap is slow, manual and permanent.

## Processes and System Calls

### Processes

- Processes have three components
  - Code - they need source code
  - Memory
    - need memory to keep track of changing state
    - this where the code, the stack and the heap live for each process
  - CPU time
    - The CPU is the only thing that execute instructions
    - The number of cores your CPU is equal to the number of things it can do at once.
    - Our computers run hundreds of processes at one time by time sharing between between each process.

### System Calls

#### Process Hierarchy

1. Hardware - devices, memory, files, hard drive
2. Privileged processes - Operating System
   - Hardware can only be accessed through the operating system.
3. Normal processes
   - Normal processes can only access the hardware by doing _system calls_ to the operating system.

#### System Calls

- System calls can be thought of as API calls from programs to your operating system.
  - Imagine a webapp with a SQL database
  - We could access the SQL database directly from our web client, but that would be insecure and leave us vulnerable to SQL injections.
  - Instead we create a REST API that acts as an intermediary between the client and the database that is accessed through HTTP requests.
  - This way, our client can only read/write to our database based on the limitations we define.
  - Client->API->Database:Processes->System Calls->OS->Hardware
  - It would be very insecure to let programs access the hardware directly, so our OS exposes system calls to each process to allow safe interaction between processes and hardware.
