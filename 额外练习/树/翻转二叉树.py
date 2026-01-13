from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def from_list_to_tree(arr: list, p: int, q: int):
    root = TreeNode(arr[0])
    deq = deque()
    node = root
    p_node = None
    q_node = None
    for i in arr[1:]:
        if node.left and node.right:
            if node.val == p:
                p_node = node
            if node.val == q:
                q_node = node
            node = deq.popleft()
        children_node = TreeNode(i)
        if not node.left:
            node.left = children_node
        elif not node.right:
            node.right = children_node
        deq.append(children_node)