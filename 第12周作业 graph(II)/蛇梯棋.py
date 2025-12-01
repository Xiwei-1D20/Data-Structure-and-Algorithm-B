from typing import List, Optional
from collections import deque

class Solution:


    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def board_to_index(n: int):
            board_of_index = [None] * (n ** 2)
            index = 0
            for i in range(n - 1, -1, -1):
                if (n - 1 - i) % 2 == 0:
                    for j in range(n):
                        board_of_index[index] = (i, j)
                        index += 1
                else:
                    for j in range(n - 1, -1, -1):
                        board_of_index[index] = (i, j)
                        index += 1
            return board_of_index

        index_of_board = board_to_index(n)

        def dfs():
            q = deque([[0, 0]])
            visited = {0}
            while q:
                index0 = q.popleft()
                for i in range(1, 7):
                    index1 = index0[0] + i
                    step = index0[1] + 1
                    if index1 == n**2 - 1:
                        return step
                    elif index1 not in visited:
                        node = board[index_of_board[index1][0]][index_of_board[index1][1]] - 1
                        visited.add(index1)
                        if node == -2:
                            q.append([index1, step])
                        else:
                            if node == n**2 - 1:
                                return step
                            q.append([node, step])

            return -1
        return dfs()



if __name__ == '__main__':
    solut = Solution()
    print(solut.snakesAndLadders([[-1,1,1,1],[-1,7,1,1],[1,1,1,1],[-1,1,9,1]]))