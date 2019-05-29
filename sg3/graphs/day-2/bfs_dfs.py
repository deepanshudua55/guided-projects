from collections import deque


class Queue:
    def __init__(self):
        self.storage = deque()

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

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
        path = []
        # create a set to store our visited vertices
        visited = set()
        # While our queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            path.append(v)
            # If that vertex has not been visited
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Add all of its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)
        return path

    def dft(self, starting_vertex_id):
        # create an empty stack
        s = Stack()
        s.push(starting_vertex_id)
        visited = set()
        path = []
        while s.size() > 0:
            v = s.pop()
            path.append(v)
            if v not in visited:
                visited.add(v)
                for next_vert in self.vertices[v]:
                    s.push(next_vert)
        return path

    """  
        instead of storing each vertex in the queue, store the path to that vertex in the queue
        when you dequeue look at the last node
        when enqueue, make a copy of the path, add that neighbor node to the new path
        enqueue the new path
    """

    def dft_recursive(self, starting_vertex_id, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # create our visited set
        if visited is None:
             visited = set()
        # add our starting id to the visited set
        visited.add(starting_vertex_id)
        for next_vert in self.vertices[starting_vertex_id]:
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
        

    def bfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create en empty queue and enqueue a PATH to the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex_id])
        # create a set for the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # grab the last vertex from that path (last index in the list)
            v = path[-1]
            # if it hasn't been visited
            if v not in visited:
                # check if its the target
                if v == destination_vertex_id:
                    # if so, return the path
                    return path
                # mark it as visited
                # if we get here we haven't reached our destination
                visited.add(v)
                # add the path to the its neighbors to the back of the queue
                for next_vert in self.vertices[v]:
                    # copy the path
                    new_path = list(path)
                    # append the neighbor to the back
                    new_path.append(next_vert)
                    # add it to the queue
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # push a list of our starting vertex id
        # on to the stack
        s.push([starting_vertex_id])
        # make a visited set
        visited = set()
        # while our stack is not empty
        while s.size() > 0:
            # pop our last path from the stack
            path = s.pop()
            # set the current vertex to be the last id in the path
            v = path[-1]
            # if it hasn't been visited...
            if v not in visited:
                # if we've reached our destination
                if v == destination_vertex_id:
                    return path
                # if it isn't the target, add to visited set
                visited.add(v)
                # loop through its neighbors
                # add a new path with each of them to the stack
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None
    
    def dfs_recursive(self, starting_vertex_id, destination_vertex_id, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # add our starting vertex id to the set
        visited.add(starting_vertex_id)
        # create a new a path with the current path and the starting vertex id
        path = path + [starting_vertex_id]
        # if our starting id is the destination
        # our base case
        if starting_vertex_id == destination_vertex_id:
            return path
        # loop through the child vertices of our current vertex
        for next_vert in self.vertices[starting_vertex_id]:
            # if our vertex hasn't been visited
            if starting_vertex_id not in visited:
                new_path = self.dfs_recursive(next_vert, destination_vertex_id, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(graph.bft(1))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))

