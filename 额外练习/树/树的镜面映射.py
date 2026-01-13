from collections import deque

class BinaryTreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.children = []


n = int(input())
nodes = input().split()
treenode_list = {}
q = deque()
for i in nodes:
    if i[0] != '$':
        q.append((BinaryTreeNode(i[0]), int(i[1])))
        treenode_list[i[0]] = TreeNode(i[0])
    else:
        q.append((None, 1))

# print(q)
# print(treenode_list)

def preorder_to_binarytree(node, in_or_out):
    # if node:
        # print(node.val, in_or_out)
    if in_or_out == 0:
        left = q.popleft()
        node.left = preorder_to_binarytree(left[0], left[1])
        right = q.popleft()
        node.right = preorder_to_binarytree(right[0], right[1])
    return node


root, in_or_out_root = q.popleft()
binary_root = preorder_to_binarytree(root, in_or_out_root)
# print(q, binary_root.val)

q1 = deque([binary_root])
# print(q1)

# 将伪满二叉树转化为正常的树
while q1:
    temp_binary_node = q1.popleft()
    temp_treenode = treenode_list[temp_binary_node.val]
    if temp_binary_node.left:
        temp_binary_node = temp_binary_node.left
        while 1:
            child = temp_binary_node.val
            # print(child, temp_binary_node.left, temp_binary_node.right)
            temp_treenode.children.append(treenode_list[child])
            if temp_binary_node.left:
                q1.append(temp_binary_node)
            if temp_binary_node.right:
                temp_binary_node = temp_binary_node.right
            else:
                break

tree_root = treenode_list[binary_root.val]


# 翻转树：
def inverse_tree(node: TreeNode):
    # print(node.children)
    new_children = []
    for _ in range(len(node.children)):
        child = inverse_tree(node.children.pop())
        new_children.append(child)
    node.children = new_children
    return node


tree_root = inverse_tree(tree_root)
q2 = deque()
q2.append(tree_root)
ans = []

# 按层遍历
while q2:
    for i in range(len(q2)):
        temp_treenode = q2.popleft()
        ans.append(temp_treenode.val)
        for j in temp_treenode.children:
            q2.append(j)

print(' '.join(ans))



