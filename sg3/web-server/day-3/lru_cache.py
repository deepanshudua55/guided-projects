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
        pass


"""
  Retrieves the value of the node given the key. Moves the
  retrieved node to the end of self.order. Should be an 
  O(1) operation.
"""


def get(self, key):
    pass


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
    pass


if __name__ == '__main__':
    cache = LRUCache(3)

    cache.put('cat.jpg', 'a')
    cache.put('index.html', 'b')
    cache.put('404.html', 'c')

    print(cache.get('cat.jpg'))
    print(cache.get('index.html'))
    print(cache.get('404.html'))

    cache.put('index.html', 'z')

    print(cache.get('index.html'))

    cache.put('foo.bar', 'd')

    print(cache.get('cat.jpg'))
