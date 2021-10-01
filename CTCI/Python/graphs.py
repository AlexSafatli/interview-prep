from stacks_queues import Stack


class Graph(object):
    def __init__(self):
        self.adj = dict()
        self.next = 0
        self.size = 0

    def get_neighbors(self, i):
        return self.adj[i]

    def get_edges_for(self, i):
        return [(i, j) for j in self.adj[i]]

    def add_edge(self, i, j):
        self.adj[i].append(j)

    def remove_edge(self, i, j):
        if j in self.adj[i]:
            self.adj[i].remove(j)
        if i in self.adj[j]:
            self.adj[j].remove(i)

    def new_vertex(self):
        self.adj[self.next] = list()
        self.size += 1
        self.next += 1

    def remove_vertex(self, i):
        self.size -= 1
        for edge in self.get_edges_for(i):
            a, b = edge
            self.remove_edge(a, b)
        del self.adj[i]

    def has_path(self, i, j):
        to_search = Stack()
        searched = list()
        to_search.push(i)
        while len(to_search) > 0:
            cur = to_search.pop()
            for ne in self.get_neighbors(cur):
                if ne == j:
                    return True
                elif ne not in searched:
                    to_search.push(ne)
            searched.append(cur)
        return False


if __name__ == '__main__':
    g = Graph()
    g.new_vertex()
    g.new_vertex()
    g.new_vertex()
    g.new_vertex()
    g.new_vertex()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 2)
    g.add_edge(2, 4)
    print(g.has_path(0, 4))
    print(g.has_path(0, 3))
