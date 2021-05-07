from collections import defaultdict

class Graph:
    def __init__(self, edges):
        self.adjacency = self.build_graph(edges)

    def build_graph(self, edges):
        adjacency = defaultdict(list)
        for edge in edges:
            a, b = edge[0], edge[1]
            adjacency[a].append(b)
            adjacency[b].append(a)
        return adjacency

class BFSGraph(Graph):
    def __init__(self, adjacency):
        super().__init__(adjacency)

    def shortest_path(self, start, end):
        #simple case
        if start == end:
            return []
        
        explored = []
        queue = [[start]]

        while len(queue) > 0:
            path = queue.pop(0)
            node = path[-1]
            if node in explored:
                continue
            for neighbor in self.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path
            explored.append(node)

        return []

    def neighbors(self, id):
        return self.adjacency[id]
        

example = BFSGraph([
            ["A", "B"], ["A", "E"],
            ["A", "C"], ["B", "D"],
            ["B", "E"], ["C", "F"],
            ["C", "G"], ["D", "E"]
            ])

for test_path in [['A', 'G'],
                  ['D', 'C'],
                  ['B', 'F']]:
    
    a, b = test_path[0], test_path[1]
    print("Shortest path from %s - %s = %s" % (a, b, example.shortest_path(a, b)))


