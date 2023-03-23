# https://leetcode.com/problems/same-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        if (not p) or (not q):
            return False
        is_equal = p.val == q.val
        return all((is_equal, self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)))
