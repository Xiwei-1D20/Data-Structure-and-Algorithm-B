from collections import deque
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.firstChild = None   # 指向第一个孩子
        self.nextSibling = None  # 指向下一个兄弟

class Solution:
    def traverse(self):
        n = int(input())
        nodes = dict()

        def find_node(num):
            if num not in nodes.keys():
                nodes[num] = [TreeNode(num), 0]
            return nodes[num]

        head = None
        for i in range(n):
            temp = [int(x) for x in input().split()]
            for j in range(len(temp)-1):
                temp_node1 = find_node(temp[j])
                temp_node2 = find_node(temp[j + 1])
                if j == 0:
                    temp_node1[0].firstChild = temp_node2[0]
                else:
                    temp_node1[0].nextSibling = temp_node2[0]
                temp_node2[1] += 1
                nodes[temp[j]] = temp_node1
                nodes[temp[j+1]] = temp_node2

        for i in nodes.keys():
            if nodes[i][1] == 0:
                head = nodes[i][0]
                break

        def smallorder(root: Optional[TreeNode]):
            if not root:
                return
            q = [[root, root.data]]
            child = root.firstChild
            while child:
                q.append([child, child.data])
                child = child.nextSibling
            q = deque(sorted(q, key=lambda x: x[1]))
            while q:
                temp_node = q.popleft()
                if temp_node[0] == root:
                    print(temp_node[1])
                else:
                    smallorder(temp_node[0])

        smallorder(head)
        return 0


if __name__ == '__main__':
    solut = Solution()
    solut.traverse()