from collections import deque
from typing import List, Optional

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        ans = []
        if not root:
            return ans
        ans.append([])
        que = deque([root])
        level = 0
        node_in_level = [1,0]
        while que:
            q = que.popleft()
            node_in_level[level] -= 1
            ans[-1].append(q.val)
            if q.left:
                que.append(q.left)
                node_in_level[level+1] += 1
            if q.right:
                que.append(q.right)
                node_in_level[level+1] += 1
            if node_in_level[level] == 0 and que:
                ans.append([])
                level += 1
                node_in_level.append(0)
        return ans

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


def test_level_order():
     solution = Solution()

     # 测试用例1: [3,9,20,null,null,15,7]
     print("测试用例1: [3,9,20,null,null,15,7]")
     root1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
     result1 = solution.levelOrder(root1)
     print(f"输出: {result1}")
     print(f"期望: [[3], [9, 20], [15, 7]]")
     print(f"测试结果: {'通过' if result1 == [[3], [9, 20], [15, 7]] else '失败'}")
     print()

     # 测试用例2: [1]
     print("测试用例2: [1]")
     root2 = create_binary_tree([1])
     result2 = solution.levelOrder(root2)
     print(f"输出: {result2}")
     print(f"期望: [[1]]")
     print(f"测试结果: {'通过' if result2 == [[1]] else '失败'}")
     print()

     # 测试用例3: []
     print("测试用例3: []")
     root3 = create_binary_tree([])
     result3 = solution.levelOrder(root3)
     print(f"输出: {result3}")
     print(f"期望: []")
     print(f"测试结果: {'通过' if result3 == [] else '失败'}")
     print()

     # 额外测试用例4: 更复杂的树
     print("测试用例4: [1,2,3,4,5,6,7]")
     root4 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
     result4 = solution.levelOrder(root4)
     print(f"输出: {result4}")
     print(f"期望: [[1], [2, 3], [4, 5, 6, 7]]")
     print(f"测试结果: {'通过' if result4 == [[1], [2, 3], [4, 5, 6, 7]] else '失败'}")
     print()

     # 可视化打印二叉树（辅助理解）


def print_tree_structure(root, level=0, prefix="Root: "):
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
     print("=== 二叉树层序遍历测试 ===\n")

     # 显示第一个测试用例的树结构
     print("测试用例1的树结构:")
     root1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
     print_tree_structure(root1)
     print()

     # 运行所有测试
     test_level_order()
