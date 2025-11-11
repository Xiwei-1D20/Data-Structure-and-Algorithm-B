class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(n: int, nums: list):
    root = TreeNode(nums[0])
    def dfs(parent_node: TreeNode, node: TreeNode, index, switch):
        if index > n-1 or index is None:
            return None
        print(index, node.val, nums[index], parent_node.val)
        if nums[index] < node.val:
            node.left = TreeNode(nums[index])
            index = dfs(node, node.left, index + 1)
        if switch == 0
        if node.val < nums[index] < parent_node.val:
            node.right = TreeNode(nums[index])
            index = dfs(node, node.right, index + 1)
        if parent_node.val < nums[index] and parent_node == root:
            root.right = nums[index]

        return index, root

    if n > 1:
        root.left = TreeNode(nums[1])
        if n > 2:
            _, root = dfs(root, root.left, 2)

    return root

def postorder1(node):
    if node:
        postorder1(node.left)
        postorder1(node.right)
        print(node.val)


def postorder(node, trace):
    if node:
        trace = postorder(node.left, trace)
        trace = postorder(node.right, trace)
        trace.append(node.val)
    return trace

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    root = build_tree(n, nums)
    print(root.val)
    postorder1(root)
    #result = postorder(root, trace=[])
    #print(result)

if __name__ == '__main__':
    main()