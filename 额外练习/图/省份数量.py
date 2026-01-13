class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        n = len(isConnected)
        parent = list(range(n + 1))
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i+1, j+1)

        #print(parent)
        circle_num = set(find(x) for x in range(1, n+1))
        return len(circle_num)


if __name__ == '__main__':
    solut = Solution()
    print(solut.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
