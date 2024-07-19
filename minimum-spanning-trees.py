# This is the problem set B answer. 

class spanningtreeset:

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item]) 
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    vertices = list(graph['vertices'])
    edges = sorted(graph['edges'], key=lambda edge: edge[2])

    disjoint_set = spanningtreeset(vertices)
    mst = []

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)

    return mst


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': [
        ('A', 'B', 2),
        ('A', 'C', 3),
        ('A', 'D', 3),
        ('A', 'E', 4),
        ('B', 'C', 1),
        ('B', 'D', 4),
        ('B', 'E', 2),
        ('C', 'D', 5),
        ('C', 'E', 1),
        ('D', 'E', 7),
        ('E', 'F', 4), 
        ('F', 'A', 1)
    ]
}

mst = kruskal(graph)
print("Test Case 3 - Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(edge)

#Coded by: Gwyn Ann S. Lobaton 
 