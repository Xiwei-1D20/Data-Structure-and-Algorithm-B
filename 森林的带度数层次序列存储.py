from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def wood(s):
    s = s.split()
    node_num_of_subnode = []
    for i in range(0,len(s),2):
        temp = [s[i],int(s[i+1])]
        node_num_of_subnode.append(temp)
    q0 = deque([node_num_of_subnode[0]])

    # 生成树
    def build_tree():
        root = TreeNode(node_num_of_subnode[0][0])
        q0 = deque([[root,node_num_of_subnode[0][1]]])
        index = 0
        while q0:
            current = q0.popleft()
            for _ in range(current[1]):
                index += 1
                child = TreeNode(node_num_of_subnode[index][0])
                q0.append([child,node_num_of_subnode[index][1]])
                current[0].children.append(child)
        return root

    head = build_tree()
    result = []

    # 利用迭代来排序
    def preorder(node: TreeNode):
        for i in node.children:
            preorder(i)
        result.append(node.val)

    preorder(head)
    return result

def main():
    n = int(input())
    result = []
    for i in range(n):
        result += wood(input())
    print(' '.join(result))

if __name__ == '__main__':
    main()