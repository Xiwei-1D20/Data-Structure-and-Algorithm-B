class Vertex:
    def __init__(self, index=None):
        self.index = index
        self.neighbors = set()


class Graph:
    def __init__(self):
        self.vertices = dict()

def build_graph(g: Graph, vert1: int, vert2: int):
    temp_vert = Vertex(vert1)
    if vert1 in g.vertices.keys():
        temp_vert = g.vertices[vert1]
    temp_vert.neighbors.add(vert2)
    g.vertices[vert1] = temp_vert

    temp_vert = Vertex(vert2)
    if vert2 in g.vertices.keys():
        temp_vert = g.vertices[vert2]
    temp_vert.neighbors.add(vert1)
    g.vertices[vert2] = temp_vert

    return g


def build_matr(n, g: Graph):
    matr = [[0 for _ in range(n)] for _ in range(n)]
    for i in g.vertices.keys():
        temp_vert = g.vertices[i]
        matr[i][i] = len(temp_vert.neighbors)
        for j in temp_vert.neighbors:
            matr[i][j] = -1
    return matr

def main():
    num, edges = [int(x) for x in input().split()]
    g0 = Graph()
    for i in range(edges):
        vert1, vert2 = [int(x) for x in input().split()]
        g0 = build_graph(g0, vert1, vert2)
    matr = build_matr(num, g0)
    for i in matr:
        print(' '.join([str(x) for x in i]))


if __name__ == '__main__':
    main()