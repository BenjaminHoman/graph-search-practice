

class Graph:
    def __init__(self, edges):
        self.edges = edges

    def neighbors(self, id):
        return self.edges[id]

example = Graph({'A': ['B'],
                 'B': ['C'],
                 'C': ['B', 'D', 'F'],
                 'D': ['C', 'E'],
                 'E': ['F'],
                 'F': []})
