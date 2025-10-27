from collections import deque
from typing import List, Optional

def edge(A:list,k):
    x=len(A[0]);y=len(A)
    for i in range(y):
        A[i]=[k]+A[i]+[k]
    A.append([k]*(x+2));A.insert(0,[k]*(x+2))
    return A


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = edge(grid, 0)
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_island = 0

        def bfs(index_x, index_y):
            que = deque([(index_x, index_y)])
            grid[index_x][index_y] = '0'
            while que:
                temp = que.popleft()
                for i in direc:
                    x1 = temp[0] + i[0]
                    y1 = temp[1] + i[1]
                    if grid[x1][y1] == '1':
                        que.append((x1, y1))
                        grid[x1][y1] = '0'
            return 1

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == '1':
                    num_island += bfs(i, j)
        return num_island

if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands(grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]))