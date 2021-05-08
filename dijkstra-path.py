import copy

class DijkstraGraph:
    def __init__(self, adjacency):
        self.adjacency = adjacency

    def init_costs(self, source):
        costs = dict()
        for key in self.adjacency.keys():
            if key == source:
                costs[key] = 0
            else:
                costs[key] = float('inf')
        return costs

    def build_path(self, search, start, end):
        node = end
        path = [end]
        while node != start:
            if node not in search:
                return []
            path.insert(0, search[node])
            node = search[node]
        return path

    def shortest_path(self, start, end):
        graph = copy.deepcopy(self.adjacency)
        costs = self.init_costs(start)
        parents = dict()

        next_node = start
        while next_node != end:
            for neighbor in graph[next_node]:
                if graph[next_node][neighbor] + costs[next_node] < costs[neighbor]:
                    costs[neighbor] = graph[next_node][neighbor] + costs[next_node]
                    parents[neighbor] = next_node

                graph[neighbor].pop(next_node)

            costs.pop(next_node)
            next_node = min(costs, key=costs.get)

        return self.build_path(parents, start, end)


if __name__ == "__main__":
    graph = DijkstraGraph({'A': {'B':1},
                           'B': {'A':1, 'F':1, 'C':2},
                           'C': {'B':2, 'D':1},
                           'D': {'C':1, 'E':2, 'G':1},
                           'E': {'D':2, 'G':1},
                           'F': {'B':1, 'G': float('inf')},
                           'G': {'F': float('inf'), 'D': float('inf'), 'E': float('inf'), 'H':1},
                           'H': {'G': float('inf'), 'I':1, 'K': 2},
                           'I': {'J':1, 'H': float('inf')},
                           'J': {'I':1, 'L': float('inf')},
                           'K': {'H':2, 'L':1},
                           'L': {'J':1, 'K':1}})
    print(graph.shortest_path('A', 'J'))

        
