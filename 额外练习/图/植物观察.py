def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


n, m = [int(x) for x in input().split()]
parent = list(range(n+1))
diff = []
for i in range(m):
    x, y, os = [int(x) for x in input().split()]
    if os == 0:
        union(x, y)
    else:
        diff.append((x, y))

for i in diff:
    nx, ny = i[0], i[1]
    if find(nx) == find(ny):
        print('NO')
        break
else:
    print('YES')
