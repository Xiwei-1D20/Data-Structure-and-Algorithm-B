from collections import deque

def build_graph(node: set, edge: set):
    graph = dict()
    for i in node:
        graph[i] = dict()
    for i in edge:
        node1, node2, length = i
        length = int(length)
        graph[node1][node2] = length
        graph[node2][node1] = length
    return graph


def dijkstra(graph: dict, nodes: set, start_node, end_node):
    result = dict()
    for i in graph.keys():
        result[i] = [[start_node], float('inf')]
    result[start_node] = [[start_node], 0]

    visited = set()

    def dfs(temp_node):
        if temp_node in visited:
            return False
        visited.add(temp_node)

        related_nodes = []
        for i in graph[temp_node].keys():
            related_node = i
            distance = graph[temp_node][i]
            related_nodes.append([related_node, distance])
            if result[related_node][1] > result[temp_node][1] + distance:
                trace = result[temp_node][0] + [related_node]
                result[related_node] = [trace, result[temp_node][1] + distance]

        if len(visited) == len(nodes):
            return True

        related_nodes.sort(key=lambda x: x[1])
        for i in related_nodes:
            if i[0] not in visited:
                dfs(i[0])

    dfs(start_node)
    result[start_node] = [[start_node, start_node], 0]
    return result[end_node]


def main():
    p = int(input())
    node = set()
    for i in range(p):
        node.add(input())

    q = int(input())
    edge = set()
    for i in range(q):
        edge.add(tuple(input().split()))

    graph = build_graph(node, edge)

    r = int(input())
    for i in range(r):
        start_node, end_node = input().split()
        result, _ = dijkstra(graph, node, start_node, end_node)
        if result[0] == result[1]:
            print(result[0])
        else:
            ans = [result[0]]
            for j in range(1, len(result)):
                last_node = result[j-1]
                now_node = result[j]
                distance = graph[last_node][now_node]
                ans.append(f'({distance})')
                ans.append(now_node)
            print('->'.join(ans))


if __name__ == '__main__':
    main()
