def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(x)] = find(y)


case = 0
while 1:
    n, m = [int(x) for x in input().split()]
    case += 1
    if not n and not m:
        break
    parent = list(range(n+1))
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        union(x, y)
    ans = len(set(find(x) for x in range(1, n+1)))
    print(f'Case {case}: {ans}')
