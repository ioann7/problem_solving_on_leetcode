# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity is O(n) where n is nodes. Space complexity is O(n) in worst case.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_minimum = float('-inf')
        stack = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if prev_minimum >= node.val:
                    return False
                prev_minimum = node.val
                current = node.right
        return True
