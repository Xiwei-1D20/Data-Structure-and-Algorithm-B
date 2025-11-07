class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    for i in range(1, len(nums)+1):
        # 易错：注意index。如果i的停止条件为len(nums) - 1，则会使最后一位数错误地被划分到right里面
        if i == len(nums) or nums[i] > root.val:
            root.left = build_tree(nums[1:i])
            root.right = build_tree(nums[i:])
            break
    return root


def postorder(node, trace):
    if node:
        trace = postorder(node.left, trace)
        trace = postorder(node.right, trace)
        trace.append(str(node.val))
    return trace


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    root = build_tree(nums)
    result = postorder(root, trace=[])
    print(' '.join(result))


if __name__ == '__main__':
    main()