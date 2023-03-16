# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_leaf(self, root: Optional[TreeNode], sum_path: int) -> None:
        if not root:
            return 0
        sum_path = (sum_path * 10) + root.val
        if not (root.left or root.right):
            return sum_path
        return self.find_leaf(root.left, sum_path) + self.find_leaf(root.right, sum_path)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.find_leaf(root, 0)
