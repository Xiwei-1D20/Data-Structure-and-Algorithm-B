from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        most_right_in_lvl = []

        def preorder(node, lvl):
            if node:
                if len(most_right_in_lvl) < lvl:
                    most_right_in_lvl.append(node.val)
                else:
                    most_right_in_lvl[lvl - 1] = node.val
                preorder(node.left, lvl + 1)
                preorder(node.right, lvl + 1)

        preorder(root, 1)
        return most_right_in_lvl
