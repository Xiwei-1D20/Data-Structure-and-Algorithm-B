from collections import deque, defaultdict
import heapq

n = int(input())
graph = defaultdict(dict)
distances = defaultdict(dict)
for i in range(n - 1):
    edge = input().split()
    parent, num = edge[0], int(edge[1])
    index0 = 0
    index1 = 1
    for j in range(num):
        index0 += 2
        index1 += 2
        child, distance = edge[index0], int(edge[index1])
        graph[parent][child] = distance
        graph[child][parent] = distance

visited = {'A'}
edge_used = 0
cost = 0
pq = []
for i in graph['A']:
    pq.append((graph['A'][i], i))
heapq.heapify(pq)

while pq and edge_used < n - 1:
    distance, node = heapq.heappop(pq)
    if node not in visited:
        visited.add(node)
        cost += distance
        edge_used += 1
        for to_node in graph[node].keys():
            if to_node not in visited:
                heapq.heappush(pq, (graph[node][to_node], to_node))

print(cost)
