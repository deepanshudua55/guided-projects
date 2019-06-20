# Hash Tables - Day 2

## Collisions

- n = total number of keys
- k = number of buckets
- Load factor = n/k
  - Keeping the load factor low keeps the chance of collisions low.
- Ideally, each bucket should have a 1/k chance of being returned from our hash function.
- Collisions are essentially inevitable.
- A bad hash function can make collisions more likely than they should be. It would favor some indices in the array over others.

## Handling Collisions

### Chaining

- Each bucket stores a linked list.
  - If a key is added to an empty bucket, it becomes the head/tail of the linked list.
  - Otherwise, a collision occurs and the new key is added to the linked list.
  - This gives us worst case O(n) performance. We must search through the whole list to get a key.
- Another option is to chain with a balanced BST, this results in worst case O(log n) performance.
- Java HashMaps use BST chaining.

### Open Addressing

- Instead of chaining, all items are stored in the table.
  - One item per slot. k must always be >= n.
- While the load factor is low, open addressing is generally superior to chaining.
  - Keeping the load factor below .7 maintains the speed of open addressing.
  - The worst case runtime of open addressing is O(n) and it rapidly grows as the load factor approaches 1.
- The hash function specifies the order of slots to probe (try) for a key.
- Python and Swift dictionaries both use open addressing.
