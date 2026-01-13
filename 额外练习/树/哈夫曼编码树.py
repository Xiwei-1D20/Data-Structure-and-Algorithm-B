import heapq


class TreeNode:
    def __init__(self, val=0, key1=None):
        self.val = val
        self.key = key1
        self.left = None
        self.right = None


n = int(input())
weights = []
for i in range(n):
    key, weight = input().split()
    weight_key = (int(weight), key, TreeNode(int(weight), {key}))
    weights.append(weight_key)


while len(weights) > 1:
    left = heapq.heappop(weights)
    right = heapq.heappop(weights)
    parent_weight = left[2].val + right[2].val
    parent_key = left[2].key | right[2].key
    parent = (parent_weight, min(parent_key), TreeNode(parent_weight, parent_key))
    parent[2].left, parent[2].right = left[2], right[2]
    heapq.heappush(weights, parent)

root = weights[0][2]
hoffman_solution = {}
solution_hoffman = {}


def preorder(node: TreeNode, code: str):
    if len(node.key) > 1:
        preorder(node.left, code + '0')
        preorder(node.right, code + '1')
    else:
        hoffman_solution[code] = list(node.key)[0]
        solution_hoffman[list(node.key)[0]] = code


preorder(root, '')

try:
    while 1:
        text = input()
        ans = ''
        if text[0] in solution_hoffman.keys():
            for i in text:
                ans += solution_hoffman[i]
        else:
            key = ''
            for i in text:
                key += i
                if key in hoffman_solution.keys():
                    ans += hoffman_solution[key]
                    key = ''
        print(ans)
except EOFError:
    pass
