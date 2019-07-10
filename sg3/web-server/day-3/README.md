# Web Server - Day 3

## LRU Cache

### Purpose

- It takes time to read files off the disk.
  - You have to call the OS, which isn't the fastest thing.
  - If you have to go to the disk for a file, it takes even longer.
- Save a copy of the file in memory so you don't have to hit the disk.

### Functions

- The LRU cache does four operations and we want to do each of these operations in O(1) time
  - Adds to the front of a list
  - Deletes from the end of a list
  - Deletes from the middle of a list
  - Finds an item in a list
- In order to do all of these things in O(1) time, we need to use a combination of a hash table and a linked list
  - Our most recently used item will be at the head of the list
    - The most recently used item was either just added or requested.
  - Our least recently used item with be at the tail
    - If the cache is full and another is added, then this item will be removed to make room.
    - We use a hash table to store key/value pairs where the key is the filename string and the value is the Linked List Node that contains the file data.
      - Accessing/searching/deleting from a hash table is O(1), while it's O(n) for a Linked List (for all nodes besides the head and tail).

### Example

```
Server Requests
---------------
index.html
style.css
bar.jpg
index.html

Cache (3 items max)
-------------------
index.html
bar.jpg
style.css

Disk
----
index.html
foo.gif
bar.jpg
style.css
bar.html
```
