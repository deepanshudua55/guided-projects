from doubly_linked_list import DoublyLinkedList

d = DoublyLinkedList

"""
Our LRUCache class keeps track of the max number of nodes it
can hold, the current number of nodes it is holding, a doubly-
linked list that holds the key-value entries in the correct
order, as well as a storage dict that provides fast access
to every node stored in the cache.
"""


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        # keep track of the size to see if we're at the limit
        self.size = 0
        # stores the order of the items in our cache
        self.order = DoublyLinkedList()
        # stores key/value pairs where key = filename, value= ListNode
        # we use the dictionary for O(1) access time
        self.storage = {}

    """
    Retrieves the value of the node given the key. Moves the
    retrieved node to the front of self.order. Should be an 
    O(1) operation.
  """

    def get(self, key):
        # check if the key is in the storage
        if key in self.storage:
            # if it is, move it to the front and return the value
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        # if it doesn't exist, return None
        else:
            return None

    """
    Sets the given key-value pair as the new tail of self.order.
    Also adds the key-value pair to the self.storage. If 
    self.order is already holding the max number of pairs, the
    head of self.order will need to be evicted before the new
    key-value pair is added. Lastly, if the key already exists
    in the cache, the old value of the key should be updated, and
    the newly-updated key-value pair should then be moved to the
    end of self.order. Should be an O(1) operation.
  """

    def put(self, key, value):
        # check if the key is in our storage
        if key in self.storage:
            node = self.storage[key]
            # overwrite the value
            node.value = (key, value)
            # move it to the front because it is the most recent
            self.order.move_to_front(node)
            return
        # if we're at capacity
        if self.size == self.limit:
            # delete the least recently used item from our storage
            del self.storage[self.order.tail.value[0]]
            # delete it from our LinkedList
            self.order.remove_from_tail()
            # decrement the size counter
            self.size -= 1
        # add our new item to the front of the LinkedList
        self.order.add_to_head((key, value))
        # add it to our storage
        self.storage[key] = self.order.head
        # increment the size
        self.size += 1


if __name__ == '__main__':
    cache = LRUCache(3)

    cache.put('cat.jpg', 'a')
    print(cache.storage)
    cache.put('index.html', 'b')
    print(cache.storage)
    cache.put('404.html', 'c')
    print(cache.storage)

    print(cache.get('cat.jpg'))
    print(cache.order)
    print(cache.get('index.html'))
    print(cache.order)
    print(cache.get('404.html'))
    print(cache.order)

    cache.put('index.html', 'z')
    print(cache.storage)

    print(cache.get('index.html'))

    cache.put('foo.bar', 'd')
    print(cache.storage)

    print(cache.get('cat.jpg'))
    print(cache.storage)
    print(cache.order)
