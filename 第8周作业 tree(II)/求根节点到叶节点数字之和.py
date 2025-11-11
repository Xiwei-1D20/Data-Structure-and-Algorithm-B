from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        trace = []
        result = []
        def backtrack(node):
            if node is None:
                return None
            trace.append(node.val)
            if node.left is None and node.right is None:
                result.append(trace[:])
            else:
                backtrack(node.left)
                backtrack(node.right)
            trace.pop()

        backtrack(root)
        sum = 0
        for i in result:
            temp = 0
            for j in range(len(i)):
                temp = temp*10 + i[j]
            sum += temp
        return sum


# 辅助函数：根据列表创建二叉树
def create_binary_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """根据层次遍历的列表创建二叉树"""
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()

        # 左子节点
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        # 右子节点
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


# 辅助函数：查找所有从根到叶的路径
def find_all_paths(root: Optional[TreeNode]) -> List[List[int]]:
    """查找所有从根节点到叶节点的路径"""
    if not root:
        return []

    result = []

    def dfs(node, path):
        if not node:
            return

        path.append(node.val)

        # 如果是叶节点，保存路径
        if not node.left and not node.right:
            result.append(path.copy())
        else:
            # 递归处理左右子树
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop()  # 回溯

    dfs(root, [])
    return result


# 测试函数
def test_sum_numbers():
    solution = Solution()

    # 测试用例1: [1,2,3]
    print("测试用例1: [1,2,3]")
    root1 = create_binary_tree([1, 2, None, 3, 4])
    result1 = solution.sumNumbers(root1)
    paths1 = find_all_paths(root1)
    print(f"所有路径: {paths1}")
    print(f"路径对应的数字: {[int(''.join(map(str, path))) for path in paths1]}")
    print(f"数字之和: {result1}")
    print(f"期望: 25")
    print(f"测试结果: {'通过' if result1 == 123 else '失败'}")
    print()

    # 测试用例2: [4,9,0,5,1]
    print("测试用例2: [4,9,0,5,1]")
    root2 = create_binary_tree([4, 9, 0, 5, 1])
    result2 = solution.sumNumbers(root2)
    paths2 = find_all_paths(root2)
    print(f"所有路径: {paths2}")
    print(f"路径对应的数字: {[int(''.join(map(str, path))) for path in paths2]}")
    print(f"数字之和: {result2}")
    print(f"期望: 1026")
    print(f"测试结果: {'通过' if result2 == 1026 else '失败'}")
    print()

    # 测试用例3: [1]
    print("测试用例3: [1]")
    root3 = create_binary_tree([1])
    result3 = solution.sumNumbers(root3)
    paths3 = find_all_paths(root3)
    print(f"所有路径: {paths3}")
    print(f"路径对应的数字: {[int(''.join(map(str, path))) for path in paths3]}")
    print(f"数字之和: {result3}")
    print(f"期望: 1")
    print(f"测试结果: {'通过' if result3 == 1 else '失败'}")
    print()

    # 额外测试用例4: [1,2,3,4,5]
    print("测试用例4: [1,2,3,4,5]")
    root4 = create_binary_tree([1, 2, 3, 4, 5])
    result4 = solution.sumNumbers(root4)
    paths4 = find_all_paths(root4)
    print(f"所有路径: {paths4}")
    print(f"路径对应的数字: {[int(''.join(map(str, path))) for path in paths4]}")
    print(f"数字之和: {result4}")
    print(f"期望: {sum([int(''.join(map(str, path))) for path in paths4])}")
    print(f"测试结果: {'通过' if result4 == sum([int(''.join(map(str, path))) for path in paths4]) else '失败'}")
    print()


# 可视化打印二叉树（辅助理解）
def print_tree_structure(root: Optional[TreeNode], level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree_structure(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_structure(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


if __name__ == "__main__":
    print("=== 求根节点到叶节点数字之和测试 ===\n")

    # 显示第一个测试用例的树结构
    print("测试用例1的树结构:")
    root1 = create_binary_tree([1,2,3,4,5])
    print_tree_structure(root1)
    print()

    # 运行所有测试
    test_sum_numbers()