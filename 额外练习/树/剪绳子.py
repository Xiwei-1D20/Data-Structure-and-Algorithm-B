import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


n = int(input())
parts = [int(x) for x in input().split()]
for i in range(n):
    parts[i] = (parts[i], TreeNode(parts[i]))
heapq.heapify(parts)
while len(parts) > 1:
    left, left_node = heapq.heappop(parts)
    right, right_node = heapq.heappop(parts)
    parent = TreeNode(left + right, left_node, right_node)
    heapq.heappush(parts, (left + right, parent))

_, root = parts[0]


def cal_weight(node):
    weight = 0
    if node.left and node.right:
        left = cal_weight(node.left)
        right = cal_weight(node.right)
        weight += (left + right + node.val)
    return weight


print(cal_weight(root))
