from collections import deque

n, m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append(list(input()))


nums = {1, 2, 3}
direct = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(x: int, y: int, island):
    if matrix[x][y] in nums:
        return
    current_island = set()
    q = deque([(x, y)])
    current_island.add((x, y))
    while q:
        from_x, from_y = q.popleft()
        for dx, dy in direct:
            to_x, to_y = from_x + dx, from_y + dy
            if -1 < to_x < n and -1 < to_y < m and (to_x, to_y) not in current_island and matrix[to_x][to_y] != '.':
                current_island.add((to_x, to_y))
                q.append((to_x, to_y))
    return current_island

islands = []
island = 1
for x in range(n):
    for y in range(m):
        if matrix[x][y] == 'X':
            if_in = 0
            for i in islands:
                if (x, y) in i:
                    if_in += 1
            if not if_in:
                islands.append(bfs(x, y, island))


def cal_manhandle(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def cal_min_distance(current_island: set):
    distance_matrix = [[float('inf') for _ in range(m)] for _ in range(n)]
    q = deque()
    for i in current_island:
        distance_matrix[i[0]][i[1]] = 0
        q.append(i)

    while q:
        from_x, from_y = q.popleft()
        for dx, dy in direct:
            to_x, to_y = from_x + dx, from_y + dy
            if -1 < to_x < n and -1 < to_y < m:
                d = 0
                if matrix[to_x][to_y] == '.':
                    d = 1
                if distance_matrix[from_x][from_y] + d < distance_matrix[to_x][to_y]:
                    distance_matrix[to_x][to_y] = distance_matrix[from_x][from_y] + d
                    q.append((to_x, to_y))
    return distance_matrix


distance_matrixs = []
for i in range(3):
    distance_matrixs.append(cal_min_distance(islands[i]))
    # for j in distance_matrixs[i]:
        # print(j)
    # print()

ans = 1000
for i in range(n):
    for j in range(m):
        distances = 0
        for k in range(3):
            distances += distance_matrixs[k][i][j]
        if matrix[i][j] == '.':
            distances -= 2
        # print(distances)
        ans = min(ans, distances)

print(ans)




