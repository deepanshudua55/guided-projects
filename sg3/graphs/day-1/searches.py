from collections import deque


class Queue:
    def __init__(self):
        self.storage = deque()

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.appendleft(item)

    def dequeue(self):
        return self.storage.popleft()


class Stack:
    def __init__(self):
        self.storage = deque()

    def size(self):
        return len(self.storage)

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        return self.storage.pop()


class Graph:
    def __init__(self):
        self.vertices = {}

    """ adds an item to the dictionary
    key is the vertex id
    value is an empty set """

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    """  
    takes in two vertex ids as arguments
    checks if both are in self.vertices
    if they are, adds the second id to the set of the first id
    """

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def bft(self, starting_vertex_id):
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store our visited vertices
        visited = set()
        # While our queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Add all of its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        # create an empty stack
        s = Stack()
        s.push(starting_vertex_id)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices(v):
                    s.push(next_vert)

    """  
        instead of storing each vertex in the queue, store the path to that vertex in the queue
        when you dequeue look at the last node
        when enqueue, make a copy of the path, add that neighbor node to the new path
        enqueue the new path
    """

    def bfs(self, starting_vertex_id, target_vertex_id):
        # create en empty queue and enqueue a PATH to the starting vertex ID
        # create a set for the visited vertices
        # while the queue is not empty
            # dequeue the first path
            # grab the last vertex from that path (last index in the list)
            # if it hasn't been visited
                # check if its the target
                    # if so, return the path
                # mark it as visited
                # add the path to the its neighbors to the back of the queue
                    # copy the path
                    # append the neighbor to the back
        pass
