from collections import deque

nodes, edges = [int(x) for x in input().split()]
graph = {}
in_degree = [0]*nodes
for i in range(nodes):
    graph[i] = set()
for i in range(edges):
    a, b = [int(x) for x in input().split()]
    if a not in graph[b]:
        graph[b].add(a)
        in_degree[a] += 1

q = deque()
result = []
temp = []
for i in range(nodes):
    if in_degree[i] == 0:
        q.append(i)
        temp.append(i)
result.append(temp)

while q:
    temp = []
    for i in range(len(q)):
        node = q.popleft()
        for j in graph[node]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.append(j)
                temp.append(j)
    result.append(temp)

ans = 0
for i in range(len(result)):
    ans += 100*len(result[i]) + len(result[i])*i

print(ans)