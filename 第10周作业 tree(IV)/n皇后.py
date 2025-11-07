from collections import deque
from typing import List, Optional

def if_ok(past_queens: list, index: int):
    for i in range(len(past_queens)):
        if index == past_queens[i] or (len(past_queens)-i) == abs(index - past_queens[i]):
            return False
    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        track = []

        def backtrack():
            for j in range(n):
                if if_ok(track, j):
                    track.append(j)
                    if len(track) == n:
                        result.append(track[:])
                    else:
                        backtrack()
                    track.pop()

        for i in range(n):
            track.append(i)
            if len(track) == n:
                result.append(track[:])
            else:
                backtrack()
            track.pop()

        result_print = []
        for i in result:
            temp_print = []
            for j in i:
                temp = ['.'] * n
                temp[j] = 'Q'
                temp_print.append(''.join(temp))
            result_print.append(temp_print)

        return result_print

if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(8))
    print(len(solution.solveNQueens(8)))