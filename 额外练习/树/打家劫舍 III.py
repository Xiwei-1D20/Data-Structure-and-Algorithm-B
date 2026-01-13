class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:

        def find_max_income(node: TreeNode):
            ans = [0, 0] # 第一个数代表包含root的最大值，第二个数代表不包含root的最大值
            if node:
                left = find_max_income(node.left)
                right = find_max_income(node.right)
                ans[0] = left[1] + right[1] + node.val
                ans[1] = max(left[0], left[1]) + max(right[0], right[1])
            return ans

        return max(find_max_income(root))
