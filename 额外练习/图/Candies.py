import heapq
from collections import defaultdict

n, m = [int(x) for x in input().split()]
maps = defaultdict(set)

for i in range(m):
    a, b, d = [int(x) for x in input().split()]
    maps[a].add((b, d))

def dijkstra(src, end):
    INF = float('inf')
    dist = {node: INF for node in range(1, n+1)}
    pq = [(0, src)]
    heapq.heapify(pq)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == end:
            break
        for node, weight in maps[u]:
            nd = d + weight
            if nd < dist[node]:
                dist[node] = nd
                heapq.heappush(pq, (nd, node))
    return dist

dist = dijkstra(1, n)
max_candies = -1
print(dist[n])