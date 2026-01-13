from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(set)
        in_degree = [0]*numCourses
        for i in prerequisites:
            y, x = i[0], i[1]

            if y not in graph[x]:
                graph[x].add(y)
                in_degree[y] += 1

        #print(in_degree)
        result = []
        def topo_sort():
            q = deque()

            for i in range(numCourses):
                if in_degree[i] == 0:
                    result.append(i)
                    q.append(i)

            while q:
                node = q.popleft()
                for i in graph[node]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        q.append(i)
                        result.append(i)

        topo_sort()
        if len(result) != numCourses:
            return []
        else:
            return result


if __name__ == '__main__':
    solut = Solution()
    print(solut.findOrder(2, [[0,1]]))