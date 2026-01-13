from collections import deque

class TreeNode:
    def __init__(self, val=0, key1=None):
        self.val = val
        self.key = key1
        self.left = None
        self.right = None


def insert(root: TreeNode, node: TreeNode):
    if not root:
        return node
    if root.val > node.val:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root

nums = [int(x) for x in input().split()]
seen = set()
seen.add(nums[0])
root = TreeNode(nums[0])

for i in nums:
    if i not in seen:
        seen.add(i)
        root = insert(root, TreeNode(i))

q = deque()
q.append(root)
ans = []
while q:
    for _ in range(len(q)):
        temp_node = q.popleft()
        ans.append(str(temp_node.val))
        if temp_node.left:
            q.append(temp_node.left)
        if temp_node.right:
            q.append(temp_node.right)

print(' '.join(ans))
