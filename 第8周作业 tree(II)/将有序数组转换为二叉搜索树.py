from collections import deque
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def backtrack(num_half: List[int]):
            if len(num_half) == 1:
                mid = TreeNode(num_half[0])
            elif len(num_half) == 2:
                mid = TreeNode(num_half[1])
                mid.left = TreeNode(num_half[0])
            elif len(num_half) == 3:
                mid = TreeNode(num_half[1])
                mid.left = TreeNode(num_half[0])
                mid.right = TreeNode(num_half[2])
            else:
                index = len(num_half)//2
                left = backtrack(num_half[:index])
                mid = TreeNode(num_half[index])
                right = backtrack(num_half[index+1:])
                mid.left = left
                mid.right = right
            return mid

        return backtrack(nums)

