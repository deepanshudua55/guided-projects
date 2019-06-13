# Processes and System Calls - Day 2

## `wait()`
- `wait()` is a system call because the parent has to _wait_ on the child in order to clean it up.
    - The first thing the parent does when it runs is clean up the child.
    - It notifies the operating system that the memory for the child can now be marked as available for other processes to use.
- Orphaned processes run after the parent ends.

## Process States
- Sleeping: the process is blocked waiting for some event, or it has been put to sleep.
- Ready to run: the process is awake and ready to be scheduled on a CPU as soon as one frees up.
- Running: the process is running on the CPU
- Zombie: the process has died and it needs to be `wait()`ed on by it its parent.

## Pipes

- You can put data in the write end of the pipe
- Then get it out from the read end
- Use the `pipe()` system call to create the pipe and get the file descriptors
- Always pipe before you fork.