from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.children = []


def build_tree(s: str):
    stack = []
    for i in s:
        if i == ')':
            temp_nodes = deque()
            temp_node = stack.pop()
            while temp_node != '(':
                temp_nodes.appendleft(temp_node)
                temp_node = stack.pop()
            else:
                stack[-1].children = list(temp_nodes)
        elif i == '(':
            stack.append('(')
        elif i != ',':
            stack.append(TreeNode(i))
    return stack[-1]


def preorder(node: TreeNode, result: str):
    result += node.val
    for i in node.children:
        result = preorder(i, result)
    return result


def postorder(node: TreeNode, result: str):
    for i in node.children:
        result = postorder(i, result)
    result += node.val
    return result

def main():
    s = input()
    root = build_tree(s)
    print(preorder(root, ''))
    print(postorder(root, ''))


if __name__ == '__main__':
    main()
