import heapq

n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

visited = set()
q = [(0, (0, 0))]
direct = ((1, 0), (-1, 0), (0, 1), (0, -1))
heapq.heapify(q)
max_diff = 0
while q:
    node = heapq.heappop(q)
    if node[1] in visited:
        continue
    max_diff = max(max_diff, node[0])
    visited.add(node[1])
    node_x, node_y = node[1]
    if node_x == n - 1 and node_y == m - 1:
        break
    for dx, dy in direct:
        index_x = node_x + dx
        index_y = node_y + dy
        if -1 < index_x < n and -1 < index_y < m and (index_x, index_y) not in visited:
            diff = abs(matrix[node_x][node_y] - matrix[index_x][index_y])
            heapq.heappush(q, (diff, (index_x, index_y)))

print(max_diff)

