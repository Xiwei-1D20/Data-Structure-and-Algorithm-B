from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []


class binaryTreeNode:
    def __init__(self, val=None, firstChild=None, bro=None):
        self.val = val
        self.firstChild = firstChild
        self.bro = bro


def dfs(s: str, node: TreeNode, index: int):
    while index < len(s):
        if s[index] == 'd':
            temp_node, index = dfs(s, TreeNode(index+1), index + 1)
            node.children.append(temp_node)
        else:
            index += 1
            return node, index
    return node, index


def tree_to_binarytree(node: TreeNode):
    binarynode = binaryTreeNode(node.val)
    if len(node.children) > 0:
        q = deque(node.children)
        temp_node_0 = tree_to_binarytree(q.popleft())
        binarynode.firstChild = temp_node_0
        for _ in range(len(node.children) - 1):
            temp_node_1 = tree_to_binarytree(q.popleft())
            temp_node_0.bro = temp_node_1
            temp_node_0 = temp_node_1

    return binarynode


def deep(node):
    if node is None:
        return 0
    if isinstance(node, TreeNode):
        depth_list = []
        for i in node.children:
            depth_list.append(deep(i))
        if len(depth_list) > 0:
            return max(depth_list) + 1
        else:
            return 0
    else:
        left_deep = deep(node.firstChild)
        right_deep = deep(node.bro)
        return max(left_deep, right_deep) + 1


def main():
    s = input()
    index = 0
    root, _ = dfs(s, TreeNode(index), index)
    depth1 = deep(root)

    binaryroot = tree_to_binarytree(root)
    depth2 = deep(binaryroot) - 1

    print(f'{depth1} => {depth2}')


if __name__ == '__main__':
    main()