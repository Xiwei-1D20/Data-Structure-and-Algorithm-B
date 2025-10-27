from collections import deque
from typing import List, Optional

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        blank_node = TreeNode(None, None, None)

        def preorder_traversal(parent_node, node, level):
            if node:
                node_left, level1 = preorder_traversal(node, node.left, level + 1)
                node_right, level2 = preorder_traversal(node, node.right, level + 1)
                if level1 == level2:
                    return node, level1
                elif level1 > level2:
                    return node_left, level1
                elif level1 < level2:
                    return node_right, level2
            else:
                return parent_node, level - 1
        ans = preorder_traversal(blank_node, root, 0)
        return ans[0]

    # 辅助函数：根据列表创建二叉树（用于测试）


def create_binary_tree(nodes):
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

# 测试函数


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


# 辅助函数：将二叉树转换为列表（层次遍历）
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """将二叉树转换为层次遍历的列表"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 移除末尾的None值
    while result and result[-1] is None:
        result.pop()

    return result


# 测试函数
def test_lca_deepest_leaves():
    solution = Solution()

    # 测试用例1: [3,5,1,6,2,0,8,null,null,7,4]
    print("测试用例1: [3,5,1,6,2,0,8,null,null,7,4]")
    root1 = create_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    result1 = solution.lcaDeepestLeaves(root1)
    print(f"最深叶节点的LCA: {result1.val}")
    print(f"期望: 2")
    print(f"测试结果: {'通过' if result1.val == 2 else '失败'}")
    print()

    # 测试用例2: [1]
    print("测试用例2: [1]")
    root2 = create_binary_tree([1])
    result2 = solution.lcaDeepestLeaves(root2)
    print(f"最深叶节点的LCA: {result2.val}")
    print(f"期望: 1")
    print(f"测试结果: {'通过' if result2.val == 1 else '失败'}")
    print()

    # 测试用例3: [0,1,3,null,2]
    print("测试用例3: [0,1,3,null,2]")
    root3 = create_binary_tree([0, 1, 3, None, 2])
    result3 = solution.lcaDeepestLeaves(root3)
    print(f"最深叶节点的LCA: {result3.val}")
    print(f"期望: 2")
    print(f"测试结果: {'通过' if result3.val == 2 else '失败'}")
    print()

    # 额外测试用例4: 平衡树
    print("测试用例4: [1,2,3,4,5,6,7]")
    root4 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    result4 = solution.lcaDeepestLeaves(root4)
    print(f"最深叶节点的LCA: {result4.val}")
    print(f"期望: 1 (整棵树都是最深叶节点，根节点是LCA)")
    print(f"测试结果: {'通过' if result4.val == 1 else '失败'}")
    print()

    # 额外测试用例5: 左斜树
    print("测试用例5: [1,2,null,3,null,4]")
    root5 = create_binary_tree([1, 2, None, 3, None, 4])
    result5 = solution.lcaDeepestLeaves(root5)
    print(f"最深叶节点的LCA: {result5.val}")
    print(f"期望: 4 (只有最深叶节点4，LCA是它自己)")
    print(f"测试结果: {'通过' if result5.val == 4 else '失败'}")
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


# 计算树的最大深度
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


# 查找所有最深叶节点
def find_deepest_leaves(root: Optional[TreeNode], depth: int, target_depth: int, result: List[TreeNode]):
    if not root:
        return

    if depth == target_depth:
        result.append(root)
        return

    find_deepest_leaves(root.left, depth + 1, target_depth, result)
    find_deepest_leaves(root.right, depth + 1, target_depth, result)


if __name__ == "__main__":
    print("=== 最深叶节点的最近公共祖先测试 ===\n")

    # 显示第一个测试用例的树结构和最深叶节点
    print("测试用例1的树结构:")
    root1 = create_binary_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print_tree_structure(root1)

    # 计算最深叶节点
    depth = max_depth(root1)
    deepest_leaves = []
    find_deepest_leaves(root1, 1, depth, deepest_leaves)
    print(f"\n最深叶节点: {[node.val for node in deepest_leaves]}")
    print(f"最大深度: {depth}")
    print()

    # 运行所有测试
    test_lca_deepest_leaves()