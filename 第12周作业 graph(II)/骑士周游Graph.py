from typing import List, Optional
from collections import deque, defaultdict


def build_graph(n: int):
    direct = [[-2, -1], [-2, 1], [2, -1], [2, 1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
    graph = dict()
    for i in range(n):
        for j in range(n):
            temp_end = set()
            for k in range(8):
                index1_x = i + direct[k][0]
                index1_y = j + direct[k][1]
                if n > index1_x >= 0 and 0 <= index1_y < n:
                    temp_end.add((index1_x, index1_y))
            graph[(i, j)] = temp_end
    return graph


def main():
    n = int(input())
    start_index_x, start_index_y = [int(x) for x in input().split()]
    graph = build_graph(n)

    def dfs(index_x, index_y, cout, visited):
        if cout == n**2:
            return visited
        point_to_visit = []
        for i in graph[(index_x, index_y)]:
            if i not in visited:
                point_to_visit.append(i)
        point_to_visit.sort(key=lambda x: len(graph[x] - (graph[x] & visited)))
        for i in point_to_visit:
            visited.add(i)
            if dfs(i[0], i[1], cout+1, visited):
                return True
            visited.discard(i)
        return False

    result = dfs(start_index_x, start_index_y, cout=1, visited={(start_index_x, start_index_y)})
    if result:
        print('success')
    else:
        print('fail')


if __name__ == '__main__':
    main()
