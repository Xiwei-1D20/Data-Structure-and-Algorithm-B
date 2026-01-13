from collections import deque

n = int(input())
for i in range(n):
    M, N = [int(x) for x in input().split()]
    matrix = []
    for _ in range(M):
        matrix.append([int(x) for x in input().split()])
    aim = [int(x) - 1 for x in input().split()]
    matrix[aim[0]][aim[1]] += 1
    water_points = []
    for _ in range(int(input())):
        water_points.append([int(x) - 1 for x in input().split()])
    # print(matrix, water_points)

    direct = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def can_overwhelm(index_x, index_y):
        height = matrix[index_x][index_y]
        matrix[index_x][index_y] = -1
        q = deque([(index_x, index_y)])
        while q:
            from_x, from_y = q.popleft()
            for dx, dy in direct:
                to_x, to_y = from_x + dx, from_y + dy
                if -1 < to_x < M and -1 < to_y < N and height >= matrix[to_x][to_y] and matrix[to_x][to_y] != -1:
                    matrix[to_x][to_y] = -1
                    q.append((to_x, to_y))

    for start_x, start_y in water_points:
        can_overwhelm(start_x, start_y)

    # print(matrix)
    if matrix[aim[0]][aim[1]] == -1:
        print('Yes')
    else:
        print('No')


