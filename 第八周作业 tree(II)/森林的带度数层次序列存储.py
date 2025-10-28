from collections import deque
from typing import List, Optional

def wood(s):
    s = s.split()
    node_num_of_subnode = []
    tree = dict()
    for i in range(0,len(s),2):
        temp = [s[i],int(s[i+1])]
        node_num_of_subnode.append(temp)
    q0 = deque(node_num_of_subnode)
    print(q0)
    #利用字典来形成树
    def backtrack(node: list):
        temp_subnodes = []
        q1 = deque()
        for i in range(node[1]):
            temp_subnode = q0.popleft()
            q1.append(temp_subnode)
            temp_subnodes.append(temp_subnode[0])
        tree[node[0]] = temp_subnodes
        for _ in range(node[1]):
            backtrack(q1.popleft())

    head = q0.popleft()
    backtrack(head)
    result = []
    print(tree)

    # 利用迭代来排序
    def preorder(node):
        for i in tree[node]:
            preorder(i)
        result.append(node)

    preorder(head[0])
    return result

def main():
    n = int(input())
    result = []
    for i in range(n):
        result += wood(input())
    print(' '.join(result))

if __name__ == '__main__':
    main()