from typing import List, Optional
from collections import deque, defaultdict

class Solution:
    def build_graph(self, n: int, words: set, g: dict):
        patterns = defaultdict(set)
        for i in words:
            temp_word = i
            for j in range(8):
                pattern = temp_word[:j] + '_' + temp_word[j + 1:]
                patterns[pattern].add(temp_word)

        for pattern in patterns.keys():
            for i in patterns[pattern]:
                g[i] = g[i] | patterns[pattern] - {i}

        return g

    def bfs(self, start: str, end: str, graph: dict):
        q = deque([[start, 0]])
        visited = {start}
        while q:
            temp_node = q.popleft()
            for i in graph[temp_node[0]]:
                if i == end:
                    return temp_node[1] + 1
                if i not in visited:
                    visited.add(i)
                    q.append([i, temp_node[1]+1])
        return -1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank0 = set(bank)
        bank0.add(startGene)
        bank0.add(endGene)
        g = dict()
        for i in bank0:
            g[i] = set()

        g = Solution.build_graph(self, len(bank0), bank0, g)

        if endGene not in bank:
            return -1

        return Solution.bfs(self, startGene, endGene, g)


if __name__ == '__main__':
    solut = Solution()
    print(solut.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]))
