class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None


n = int(input())
tree = {-1: None}
for i in range(1, n+1):
    tree[i] = TreeNode(i)
for i in range(1, n+1):
    left, right = [int(x) for x in input().split()]
    tree[i].left = tree[left]
    tree[i].right = tree[right]

def find_lvl(node, lvl):
    if node:
        lvl_left = find_lvl(node.left, lvl + 1)
        lvl_right = find_lvl(node.right, lvl + 1)
        return max(lvl_right, lvl_left)
    return lvl - 1

max_lvl = find_lvl(tree[1], 1)
print(max_lvl)
