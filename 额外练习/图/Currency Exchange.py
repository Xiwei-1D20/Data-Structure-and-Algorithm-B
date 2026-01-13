import heapq
from math import sqrt
from collections import defaultdict

inpu = input().split()
kinds, m, start_kind= [int(x) for x in inpu[0:3]]
start_num = float(inpu[3])
graph = defaultdict(dict)

for i in range(m):
    inpu = input().split()
    kind1, kind2 = [int(x) for x in inpu[0:2]]
    multi1, fee1, multi2, fee2 = [float(x) for x in inpu[2:6]]
    if kind2 not in graph[kind1].keys():
        graph[kind1][kind2] = []
    if kind1 not in graph[kind2].keys():
        graph[kind2][kind1] = []
    graph[kind1][kind2].append((multi1, fee1))
    graph[kind2][kind1].append((multi2, fee2))

# print(graph)

def bellman_ford():
    dist = [float('-inf')]*(kinds + 1)
    dist[start_kind] = start_num

    for _ in range(kinds - 1):
        for u in graph:
            for v in graph[u]:
                for multi, fee in graph[u][v]:
                    if dist[u] != float('-inf') and (dist[u] - fee) * multi > dist[v]:
                        dist[v] = (dist[u] - fee) * multi

    for u in graph:
        for v in graph[u]:
            for multi, fee in graph[u][v]:
                if dist[u] != float('-inf') and (dist[u] - fee) * multi > dist[v]:
                    dist[v] = (dist[u] - fee) * multi
                    return 1
    return 0

ans = bellman_ford()
if ans == 1:
    print('YES')
else:
    print('NO')