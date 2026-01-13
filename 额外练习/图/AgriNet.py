import heapq

while 1:
    try:
        n = int(input())
        matrix = []
        for i in range(n):
            matrix.append([int(x) for x in input().split()])

        set_index = {x for x in range(n)}
        visited = {0}
        pq = []
        for i in range(1, n):
            pq.append((matrix[0][i], i))
        heapq.heapify(pq)
        total_cost = 0
        edges_used = 0

        while pq and edges_used < n - 1:
            distance, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                edges_used += 1
                total_cost += distance
                # print(set_index - {node})
                for i in (set_index - {node}):
                    if i not in visited:
                        # print(i, node)
                        heapq.heappush(pq, (matrix[node][i], i))

        print(total_cost)
    except EOFError:
        break
