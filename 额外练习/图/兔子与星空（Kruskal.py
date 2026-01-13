from collections import deque, defaultdict
import heapq

class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1


def word_to_index(x: str):
    return ord(x) - 65


n = int(input())
graph = defaultdict(dict)
distances = defaultdict(dict)
for i in range(n - 1):
    edge = input().split()
    parent, num = word_to_index(edge[0]), int(edge[1])
    index0 = 0
    index1 = 1
    for j in range(num):
        index0 += 2
        index1 += 2
        child, distance = word_to_index(edge[index0]), int(edge[index1])
        graph[parent][child] = distance
        graph[child][parent] = distance

edges = []
for i in range(n):
    for j in range(i + 1, n):
        if j in graph[i]:
            edges.append((i, j, graph[i][j]))

edges.sort(key=lambda x : x[2])
mini_tree = []
disjoint = DisjointSet(n)
for edge in edges:
    u, v, w = edge
    if disjoint.find(u) != disjoint.find(v):
        disjoint.union(u, v)
        mini_tree.append(w)

print(sum(mini_tree))