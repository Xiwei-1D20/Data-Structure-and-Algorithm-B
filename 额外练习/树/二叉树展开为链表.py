from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        preorder_of_tree = []

        def preorder(node):
            if node:
                preorder_of_tree.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        root.val = preorder_of_tree[0]
        root.left = None
        curr = root
        for i in preorder_of_tree[1:]:
            curr.right = TreeNode(i)
            curr = curr.right



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
    return root, p_node, q_node


if __name__ == '__main__':
    solut = Solution()
    root, p, q = from_list_to_tree([1,2,5,3,4,None,6], p = 1, q = 2)
    print()
    print(solut.flatten(root))
