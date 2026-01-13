from collections import defaultdict, deque

class Vectex:
    def __init__(self, index):
        self.index = index
        self.neighbor = set()
        self.parent = None

def main():
    nodes, edges_of_1 = [int(x) for x in input().split()]
    graph = dict()
    node_not_in_tree = set()
    for i in range(1, nodes+1):
        graph[i] = Vectex(i)
        node_not_in_tree.add(i)
    for i in range(edges_of_1):
        node1, node2 = [int(x) for x in input().split()]
        graph[node1].neighbor.add(node2)
        graph[node2].neighbor.add(node1)
    start = 1
    len_all_edge = 0
    q = deque([start])
    distance_1 = graph[start].neighbor.copy()
    distance_0 = node_not_in_tree - distance_1
    while q:
        temp_node = q.popleft()
        node_not_in_tree.discard(temp_node)
        distance_1 = distance_1 & graph[temp_node].neighbor
        if node_not_in_tree:
            if len(distance_0) > 0:
                next_node = distance_0.pop()
            else:
                distance_0 = node_not_in_tree - distance_1
                if len(distance_0) > 0:
                    next_node = distance_0.pop()
                else:
                    next_node = distance_1.pop()
                    len_all_edge += 1
            q.append(next_node)
    print(len_all_edge)


if __name__ == '__main__':
    main()