# Data Structures - Day 1

## Linked Lists

- Linked Lists are composed of nodes.
  - Nodes store a value. This can be a string, integer, etc.
- Linked Lists store a variable for the head and the tail.
  - Accessing the head or the tail is O(1)
  - Accessing all other nodes is O(n)

### Singly Linked List

- Nodes only know about what is behind them, or the next node in the list.
- Can only be traversed in one direction.
- Removing from the head is O(1)
- Removing from the tail is O(n)

## Arrays vs. Linked Lists

- An array is a contiguous block of memory.
  ```python
  l = ['a', 'b', 'c']
  """
    Ex. 1
  100 - 'a'
  101 - 'b'
  102 - 'c'
  We remove 'a'
  100 - Nothing
  101 - 'b'
  102 - 'c'
  We shift b and c one spot over
  100 - 'b'
  101 - 'c'
  102 - Nothing
  Ex. 2
  Insert 'd'
  100 - 'd'
  101 - 'a'
  102 - 'b'
  103 - 'c'
  """
  ```
