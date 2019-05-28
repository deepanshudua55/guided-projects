""" 
Adjacency list 
A representation of a graph as a dictionary of vertices mapping labels to edges.
"""


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
