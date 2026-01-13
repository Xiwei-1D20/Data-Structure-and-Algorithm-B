n, m, L = [int(x) for x in input().split()]
graph = {}
for i in range(n):
    graph[i] = []
for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    graph[i].sort()
visited = set()
trace = []
start = int(input())


def dfs(node, lvl):
    if lvl > L:
        return
    visited.add(node)
    trace.append(str(node))
    for child in graph[node]:
        if child not in visited:
            dfs(child, lvl + 1)


dfs(start, 0)
print(' '.join(trace))
