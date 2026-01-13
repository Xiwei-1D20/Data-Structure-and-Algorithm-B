import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().split()[0])
for i in range(n):
    nodes, edges = [int(x) for x in sys.stdin.readline().split()]
    graph = defaultdict(set)
    in_degree = [0]*(nodes + 1)
    result = 0
    for _ in range(edges):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if b not in graph[a]:
            graph[a].add(b)
            in_degree[b] += 1

    q = deque()
    for j in range(1, nodes + 1):
        if in_degree[j] == 0:
            q.append(j)
            result += 1

    while q:
        node = q.popleft()
        for j in graph[node]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.append(j)
                result += 1

    if result == nodes:
        print('No')
    else:
        print('Yes')
