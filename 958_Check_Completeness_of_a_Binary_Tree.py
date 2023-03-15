# https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def save_root_numbers(self, root: Optional[TreeNode], 
                          number_vertox: int, save: List[int]) -> None:
        if not root:
            return
        save.append(number_vertox)
        self.save_root_numbers(root.left, number_vertox * 2, save)
        self.save_root_numbers(root.right, (number_vertox * 2) + 1, save)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.save_root_numbers(root, 1, result)
        if max(result) > len(result):
            return False
        return True
