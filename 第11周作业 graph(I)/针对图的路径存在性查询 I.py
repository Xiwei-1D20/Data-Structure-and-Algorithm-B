from typing import List, Optional
from collections import deque

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        graph = [0]*n
        for i in range(1,n):
            graph[i] = graph[i-1]
            if nums[i] - nums[i-1] > maxDiff:
                graph[i] += 1
        ans = [False]*len(queries)
        for i in range(len(queries)):
            ans[i] = (graph[queries[i][0]] == graph[queries[i][1]])
        return ans

if __name__ == '__main__':
    solut = Solution()
    print(solut.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]))