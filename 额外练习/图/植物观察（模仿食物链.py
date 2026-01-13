def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


n, m = [int(x) for x in input().split()]
parent = list(range(2*n))
for i in range(m):
    x, y, os = [int(x) for x in input().split()]
    if os == 0:
        if find(x) != find(y + n) or find(y) != find(x + n):
            union(x, y)
            union(x + n, y + n)
        else:
            print('NO')
            break
    else:
        if find(x) != find(y):
            union(x, y + n)
            union(x + n, y)
        else:
            print('NO')
            break
else:
    print('YES')
