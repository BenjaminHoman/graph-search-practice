import copy

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def build_path(self):
        if self.parent is not None:
            return self.parent.build_path() + [self.position]
        return [self.position]

class AStarGrid:
    def __init__(self, grid):
        self.grid = grid

    def neighbors(self, node):
        adjacency_vectors = [(0, -1), (0, 1),
                             (-1, 0), (1, 0),
                             (-1, -1), (-1, 1),
                             (1, -1), (1, 1)]

        for vector in adjacency_vectors:
            node_pos = self.add_positions(node.position, vector)

            if self.is_out_of_bounds(node_pos) or not self.is_walkable(node_pos):
                continue

            yield Node(node, node_pos)

    def is_out_of_bounds(self, pos):
        return pos[0] > (len(self.grid)-1) or pos[0] < 0 or pos[1] > (len(self.grid[0])-1) or pos[1] < 0

    def is_walkable(self, pos):
        return self.grid[pos[0]][pos[1]] == 0

    def add_positions(self, pos_a, pos_b):
        return (pos_a[0]+pos_b[0], pos_a[1]+pos_b[1])

    def get_current_node(self, open_list):
        current_node, current_index = open_list[0], 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index
        return current_node, current_index

    def heuristic(self, node, end):
        return ((node.position[0] - end.position[0]) ** 2) + ((node.position[1] - end.position[1]) ** 2)

    def shortest_path(self, start, end):
        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:
            current_node, current_index = self.get_current_node(open_list)

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                return current_node.build_path()

            # Loop through children
            for child in self.neighbors(current_node):
                if child in closed_list:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = self.heuristic(child, end_node)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

        # no path found
        return []

class AStarGridDebug(AStarGrid):
    def __init__(self, grid):
        super().__init__(grid)

    def debug(self, start, end):
        path = self.shortest_path(start, end)
        debug_grid = copy.copy(self.grid)
        for node in path:
            a, b = node[0], node[1]
            debug_grid[a][b] = 'X'
        self.print_grid(debug_grid)

    def print_grid(self, grid):
        s = [[str(e) for e in row] for row in grid]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (8, 3)

    #path = astar(maze, start, end)
    #print(path)

    graph = AStarGridDebug(maze)
    graph.debug(start, end)
