from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(set)
    def add_edge(self, u, v):
        self.edges[u].add(v)
        self.edges[v].add(u)
    def get_nbrs(self, u):
        return self.edges[u]

graph = Graph()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        u, v = line.strip().split('-')
        graph.add_edge(u, v)

# part 1
result = 0
for u in graph.edges:
    for v in graph.edges[u]:
        for w in graph.edges[u]:
            if w == v:
                continue
            if v in graph.edges[w]:
                result += any(node.startswith('t') for node in (u, v, w))
print(result//6)


def max_clique(nodes):
    if len(nodes) == 0:
        return set()
    if len(nodes) == 1:
        return nodes
    temp_nodes = nodes.copy()
    node = temp_nodes.pop()
    clique_without = max_clique(temp_nodes)
    clique_with = max_clique(graph.edges[node] & temp_nodes) | {node}
    return clique_with if len(clique_with) > len(clique_without) else clique_without

# part 2
nodes = set(graph.edges.keys())
result = ','.join(x for x in sorted(max_clique(nodes)))
print(result)