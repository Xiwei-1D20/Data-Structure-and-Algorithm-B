from collections import defaultdict, deque

class Vertex:
    def __init__(self, index):
        self.index = index
        self.start = None
        self.u = None
        self.innode = defaultdict(int)
        self.num_innode = 0
        self.outnode = defaultdict(int)
        self.num_outnode = 0

def main():
    n, p = [int(x) for x in input().split()]
    graph = dict()

    def build_graph():
        for i in range(n):
            start, u = [int(x) for x in input().split()]
            temp_vertex = Vertex(i+1)
            temp_vertex.start = start
            temp_vertex.u = u
            graph[i+1] = temp_vertex
        for i in range(p):
            from_node, to_node, weight = [int(x) for x in input().split()]
            graph[from_node].outnode[to_node] += weight
            graph[to_node].innode[from_node] += weight
        for i in range(n):
            graph[i+1].num_outnode = len(graph[i+1].outnode.keys())
            graph[i+1].num_innode = len(graph[i+1].innode.keys())

    build_graph()

    def topological_sort():
        result_sort = []
        q = deque()
        innode_set = set()
        for i in range(n):
            if graph[i + 1].num_innode == 0:
                q.append(i + 1)
                innode_set.add(i + 1)

        while q:
            temp_node = q.popleft()
            result_sort.append(temp_node)
            for i in graph[temp_node].outnode.keys():
                graph[i].num_innode -= 1
                if graph[i].num_innode == 0:
                    q.append(i)

        if len(result_sort) != len(graph.keys()):
            return 0

        result_C = [0]*(n+1)
        for i in result_sort:
            if (i in innode_set) and graph[i].start > 0:
                result_C[i] = graph[i].start
            elif i not in innode_set and result_C[i] - graph[i].u> 0:
                result_C[i] -= graph[i].u
            else:
                result_C[i] -= graph[i].u
                continue
            for j in graph[i].outnode.keys():
                result_C[j] += result_C[i]*graph[i].outnode[j]

        ans = []
        for i in range(1, n+1):
            if result_C[i] > 0 and graph[i].num_outnode == 0:
                ans.append([str(i), str(result_C[i])])
        ans.sort(key=lambda x:int(x[0]))
        return ans

    ans = topological_sort()
    if ans == 0 or ans == []:
        print('NULL')
    else:
        for i in ans:
            print(' '.join(i))


if __name__ == "__main__":
    main()
