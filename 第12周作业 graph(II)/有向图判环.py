class Vertex:
    def __init__(self, index=None):
        self.index = index
        self.out = set()


class Graph:
    def __init__(self):
        self.vertices = dict()


def main():
    n, m = [int(x) for x in input().split()]
    g = Graph()
    for i in range(n):
        g.vertices[i] = Vertex(i)
    for i in range(m):
        vert1, vert2 = [int(x) for x in input().split()]
        g.vertices[vert1].out.add(vert2)


    visited = set()
    visited_in_one_dfs = []

    def dfs(vert: int):
        # print(vert)
        # print(visited, visited_in_one_dfs)
        if vert in visited:
            return False
        elif vert in visited_in_one_dfs:
            return True
        else:
            visited_in_one_dfs.append(vert)
            if len(g.vertices[vert].out) > 0:
                for i in g.vertices[vert].out:
                    if dfs(i):
                        return True
            visited.add(visited_in_one_dfs.pop())

    for i in g.vertices.keys():
        if dfs(i):
            print('Yes')
            break
    else:
        print('No')



if __name__ == '__main__':
    main()

