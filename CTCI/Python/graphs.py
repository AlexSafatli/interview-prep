from stacks_queues import Stack


class DirectionalGraph(object):
    def __init__(self):
        self.adj: dict = {}
        self.size = 0

    def add_vertex(self, key):
        self.adj[key] = []
        self.size += 1

    def __len__(self) -> int:
        return self.size

    def get_neighbors(self, key) -> list:
        return self.adj[key]

    def add_edge(self, key_1, key_2):
        self.adj[key_1].append(key_2)

    def has_path(self, key_1, key_2):
        return len(self.get_path(key_1, key_2)) > 0

    def get_path(self, key_1, key_2) -> list:
        # DFS uses Stack, BFS uses Queue
        stack = Stack()
        visited = []
        stack.push((key_1, []))
        while len(stack):
            cur, path = stack.pop()
            path.append(cur)
            for nei in self.get_neighbors(cur):
                if nei == key_2:
                    path.append(nei)
                    return path
                elif nei not in visited:
                    stack.push((nei, [_ for _ in path]))
                    visited.append(nei)
        return []


if __name__ == '__main__':
    g = DirectionalGraph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 2)
    g.add_edge(2, 4)
    print(g.has_path(0, 4))
    print(g.has_path(0, 3))
    print(g.get_path(0, 4))
