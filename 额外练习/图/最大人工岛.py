from collections import defaultdict

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        def find(index_x, index_y):
            if parent[index_x][index_y] != (index_x, index_y):
                parent_x, parent_y = parent[index_x][index_y]
                parent[index_x][index_y] = find(parent_x, parent_y)
            return parent[index_x][index_y]

        def union(p: tuple, q: tuple):
            p_x, p_y = p
            q_x, q_y = q
            parent_p_x, parent_p_y = find(p_x, p_y)
            parent_q_x, parent_q_y = find(q_x, q_y)
            parent[parent_q_x][parent_q_y] = (parent_p_x, parent_p_y)

        n = len(grid)
        parent = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                parent[i][j] = (i, j)

        # 并查所有联通的块
        parents = defaultdict(int)
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    parent[i][j] = None
                else:
                    grid[i][j] = 0
                    for dx, dy in direct:
                        index_x = i + dx
                        index_y = j + dy
                        if -1 < index_x < n and -1 < index_y < n and grid[index_x][index_y] == 1:
                            #print((i, j), (index_x, index_y))
                            union((i, j), (index_x, index_y))
                #print(grid, parent)


        for i in range(n):
            for j in range(n):
                if parent[i][j]:
                    parents[find(i, j)] += 1

        #print(parents, parent)
        if parents:
            ans = max(parents.values())
        else:
            ans = 0
        for i in range(n):
            for j in range(n):
                if not parent[i][j]:
                    temp_ans = 1
                    near_parents = set()
                    for dx, dy in direct:
                        index_x = i + dx
                        index_y = j + dy
                        if -1 < index_x < n and -1 < index_y < n and parent[index_x][index_y]:
                            near_parents.add(parent[index_x][index_y])
                    for near_parent in near_parents:
                        temp_ans += parents[near_parent]
                    ans = max(ans, temp_ans)
        return ans





if __name__ == '__main__':
    solut = Solution()
    print(solut.largestIsland([[0,1],[1,1]]))