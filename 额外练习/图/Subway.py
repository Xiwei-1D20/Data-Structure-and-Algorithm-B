import heapq
from math import sqrt
from collections import defaultdict

def cal_time(a: tuple, b:tuple, speed):
    a_x, a_y = a[0], a[1]
    b_x, b_y = b[0], b[1]
    distance = sqrt(abs(a_x - b_x) ** 2 + abs(a_y - b_y) ** 2)
    speed_m_min = speed * 1000 / 60
    return distance / speed_m_min

origin = [int(x) for x in input().split()]
start, end = (origin[0], origin[1]), (origin[2], origin[3])

lines = []
node = [start, end]

graph = defaultdict(dict)

while 1:
    try:
        inpu = input().split()
        if not inpu:
            break
        line = [int(x) for x in inpu]
        node_in_line = []
        for i in range(0, len(line) - 2, 2):
            now = (line[i], line[i + 1])
            if len(node_in_line):
                time = cal_time(now, node_in_line[-1], 40)
                graph[now][node_in_line[-1]] = time
                graph[node_in_line[-1]][now] = time
            node.append(now)
            node_in_line.append(now)

        lines.append(node_in_line)
    except EOFError:
        break

for i in range(len(node)):
    for j in range(i + 1, len(node)):
        from_node, to_node = node[i], node[j]
        if to_node not in graph[from_node].keys():
            time = cal_time(from_node, to_node, 10)
            graph[from_node][to_node] = time
            graph[to_node][from_node] = time


def dijkstra(start, end):
    INF = float('inf')
    dist = {index: INF for index in node}
    ways = {index: [] for index in node}
    pq = [(0, start)]
    heapq.heapify(pq)
    while pq:
        # print(pq)
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == end:
            break
        for v in graph[u].keys():
            nd = d + graph[u][v]
            if nd < dist[v]:
                dist[v] = nd
                ways[v] = list(ways[u]) + [u]
                heapq.heappush(pq, (nd, v))
    return dist, ways

dist, ways = dijkstra(start, end)
print(round(dist[end]))
