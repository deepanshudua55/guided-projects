from collections import deque
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],  # islands[1][1] is the second one in this lists
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]] 

# islands[y][x]

islands[2][1]

"""  
How to solve any graphs problem
1. Translate the problem into terminology you've learned this week.
2. Build your graph.
3. Traverse the graph.
"""

class Stack:
    def __init__(self):
        self.storage = deque()

    def size(self):
        return len(self.storage)

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        return self.storage.pop()

def get_neighbors(coordinates, graph_matrix):
    x, y = coordinates
    neighbors = []
    # check in each cardinal direction
    # if we find a 1, append it to neighbors
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y -1 ))
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1 ))
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x-1, y))
    if x < len(graph_matrix[0]) -1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y ))
    return neighbors

def dft(x, y, matrix, visited):
    # create our stack
    s = Stack()
    # push a tuple of the starting vertex to the stack
    s.push((x, y))
    # while our stack is not empty
    while s.size() > 0:
        # pop the first vertex
        x, y = s.pop()
        #  if it hasn't been visited
        if not visited[y][x]:
            # mark the element in the visited array as True
            visited[y][x] = True
            # push all its neighbors on to the end of the stack
            # get neighbors finds all occurrences of "1" that haven't
            for neighbor in get_neighbors((x, y), matrix):
                s.push(neighbor)
    return visited
 

def island_counter(matrix):
    # create a variable for the count
    island_count = 0
    # Create a visited matrix
    visited = [[False] * len(arr) for arr in matrix]
    # for arr in visited:
    #     print(arr)
    # Walk through each cell in the matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # if the current element hasn't been visited
            if not visited[y][x]:
                # check if the current element is a 1
                    # if it is do a dft
                if matrix[y][x] == 1:
                    visited = dft(x, y, matrix, visited)
                    # increment the counter by 1
                    island_count += 1
    return island_count




island_counter(islands)  # returns 13
