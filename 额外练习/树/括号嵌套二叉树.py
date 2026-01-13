class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


n = int(input())
for i in range(n):
    input_str = input()
    tree = []
    for i in input_str:
        if i != ',':
            tree.append(i)
    stack = []
    for j in range(len(tree)):
        if tree[j] == '(':
            continue
        elif tree[j] == ')':
            right = stack.pop()
            left = stack.pop()
            stack[-1].left = left
            stack[-1].right = right
        elif tree[j] == '*':
            stack.append(None)
        else:
            stack.append(TreeNode(tree[j]))

    root = stack[-1]

    preorder_list = []
    midorder_list = []

    def preorder(node: TreeNode):
        if node:
            preorder_list.append(node.val)
            preorder(node.left)
            preorder(node.right)

    def midorder(node: TreeNode):
        if node:
            midorder(node.left)
            midorder_list.append(node.val)
            midorder(node.right)

    preorder(root)
    midorder(root)

    print(''.join(preorder_list))
    print(''.join(midorder_list))
