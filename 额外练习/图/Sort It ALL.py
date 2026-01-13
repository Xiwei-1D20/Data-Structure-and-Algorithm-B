from collections import defaultdict, deque

def topo_sort(graph1):
    q = deque()
    result = []
    in_degree1 = {u:0 for u in graph1}
    # print(graph1, in_degree1)
    for u in graph1:
        for v in graph1[u]:
            in_degree1[v] += 1

    for i in range(nodes):
        if in_degree1[i] == 0:
            q.append(i)
            result.append(i)
    flag = 0
    while q:
        # print(q)
        if len(q) > 1:
            flag = 1
        node = q.popleft()
        for i in graph[node]:
            in_degree1[i] -= 1
            if in_degree1[i] == 0:
                q.append(i)
                result.append(i)

    # print(result, graph1.keys())
    if len(result) != len(graph1.keys()):
        return 1, []
    else:
        if flag == 1:
            return -1, []
        if len(result) == nodes:
            return 0, result
    return -1, []


while 1:
    nodes, edge = [int(x) for x in input().split()]
    if nodes == 0 and edge == 0:
        break

    def word_to_num(x: str):
        return ord(x) - 65

    def num_to_word(x: int):
        return chr(x + 65)


    # graph = defaultdict(set)
    graph = {x: set() for x in range(nodes)}
    ends = -1
    count = 0
    edges = []
    for i in range(edge):
        a, b = input().split('<')
        a1, b1 = word_to_num(a), word_to_num(b)
        edges.append((a1, b1))

    # print(graph)
    for i in range(edge):
        a1, b1 = edges[i]
        count += 1
        if a1 not in graph[b1]:
            graph[b1].add(a1)
            # print(graph, in_degree)
            ends, result = topo_sort(graph)
            if ends == 1 or ends == 0:
                break
    else:
        print('Sorted sequence cannot be determined.')

    if ends == 1:
        print(f'Inconsistency found after {count} relations.')
        continue
    elif ends == 0:
        result.reverse()
        ans = ''
        for i in result:
            ans += num_to_word(i)
        print(f'Sorted sequence determined after {count} relations: ' + ans + '.')

    '''
    q = deque()
    result = []
    for i in range(nodes):
        if in_degree[i] == 0:
            q.append(i)
            result.append(i)

    end_index = 0
    while q:
        if len(q) > 1:
            end_index = 1
            break
        node = q.popleft()
        for i in graph[node]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
                result.append(i)


    if end_index == 0:
        result.reverse()
        ans = ''
        for i in result:
            ans += num_to_word(i)
        print(f'Sorted sequence determined after {nodes} relations: '+ans+'.')
    elif end_index == 1:
        print('Sorted sequence cannot be determined.')
    '''