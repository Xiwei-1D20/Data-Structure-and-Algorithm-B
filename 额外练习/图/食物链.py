def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


n, m = [int(x) for x in input().split()]
parent = list(range(3*n+1))
wrong = 0
for i in range(m):
    os, x, y = [int(x) for x in input().split()]
    if x > n or y > n:
        wrong += 1
    elif os == 2 and x == y:
        wrong += 1
    elif os == 1:
        if find(x) == find(y + n) or find(x) == find(y + 2*n):
            wrong += 1
            continue
        union(x, y)
        union(x + n, y + n)
        union(x + 2*n, y + 2*n)
    elif os == 2:
        if find(x) == find(y) or find(x) == find(y + 2*n):
            wrong += 1
            continue
        union(x, y + n)
        union(x + n, y + 2*n)
        union(x + 2*n, y)

print(wrong)