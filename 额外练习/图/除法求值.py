from collections import deque

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = {}
        for i in equations:
            for j in i:
                if j not in graph.keys():
                    graph[j] = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i]

        #print(graph)
        def dfs(x, y):
            #print()
            #print(x, y)
            q = deque([(x, 1)])
            visited = {x}
            while q:
                #print(q)
                num, result = q.popleft()
                for i in graph[num].keys():
                    #print(i)
                    if i == y:
                        return result * graph[num][i]
                    elif i not in visited:
                        q.append((i, result * graph[num][i]))
                        visited.add(i)
            return float(-1)

        ans = []
        for x, y in queries:
            if x not in graph.keys() or y not in graph.keys():
                ans.append(float(-1))
            else:
                ans.append(dfs(x, y))

        return ans

if __name__ == '__main__':
    solut = Solution()
    print(solut.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))