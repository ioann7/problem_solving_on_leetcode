# https://leetcode.com/problems/maximum-depth-of-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_max_depth(root, 1)

    def get_max_depth(self, root: TreeNode, depth: int) -> int:
        left = self.get_max_depth(root.left, depth + 1) if root.left else 0
        right = self.get_max_depth(root.right, depth + 1) if root.right else 0
        return max(depth, left, right)
