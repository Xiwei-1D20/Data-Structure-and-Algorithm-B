from typing import List, Optional
from collections import deque

class Solution:

    def build_graph(self, n, nums, maxDiff: int):
        graph = dict()
        for i in list(range(n)):
            graph[i] = {i}
        for i in range(1, len(nums)):
            j = i - 1
            if abs(nums[i] - nums[j]) <= maxDiff:
                graph[j].add(i)
                graph[i] = graph[j]
        return graph

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        graph = self.build_graph(n, nums, maxDiff)
        ans = []
        for i in queries:
            ans.append(i[1] in graph[i[0]])
        return ans


if __name__ == '__main__':
    solut = Solution()
    print(solut.pathExistenceQueries(n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]))