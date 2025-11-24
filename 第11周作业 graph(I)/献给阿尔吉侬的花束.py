from collections import deque


def dfs(matr, start, r, c):
    direct = ((-1, 0), (1, 0), (0, 1), (0, -1))
    q = deque([start])
    while q:
        x0, y0, step = q.popleft()
        for i in direct:
            x1 = x0 + i[0]
            y1 = y0 + i[1]
            if x1 < 0 or y1 < 0 or x1 > r - 1 or y1 > c - 1:
                continue
            if matr[x1][y1] == 'E':
                return step + 1
            elif matr[x1][y1] == '.':
                matr[x1][y1] = '#'
                q.append((x1, y1, step + 1))


def main():
    n = int(input())
    for i in range(n):
        r, c = [int(x) for x in input().split()]
        matr = []
        for j in range(r):
            matr.append(list(input()))
        start = (0, 0, 0)
        for x in range(r):
            for y in range(c):
                if matr[x][y] == 'S':
                    start = (x, y, 0)
        result = dfs(matr, start, r, c)
        if result is not None:
            print(result)
        else:
            print('oop!')


if __name__ == '__main__':
    main()
