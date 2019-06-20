# Hash Tables - Day 1

## [Associative Arrays](https://en.wikipedia.org/wiki/Associative_array)

- It maintains a set of items, each with a key
  - insert(item) - add the item to the set, overwrite if key already exists
  - delete(item) - remove item from the set
  - search(key) - return an item with the key, if it exists
  - A balanced BST can do all of these operations in O(log n) time.
  - But we can do better, a hash table can do all of these in O(1) time.

## Hashing

- The word hash is derived from "hatchet" (an axe).
- The hash function will take in strings of variable length, and will always give us back an integer that is <= our total number of buckets.
- One approach to a hash function is using the `%` operator
  - (key) % (# of buckets)

## Usage

- Implemented in every single modern programming language.
- Used for caching - like in dynamic programming.
  - nth-Fibonacci problem is O(2^n) without caching, O(n) with caching.
- Sets - hash tables, but with only keys and no value.

## Differences with Arrays

- Under the hood, they're arrays.
- Unlike arrays, hash tables are unordered.
