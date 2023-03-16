# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        root_val = postorder.pop()
        inorder_mid_index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.right = self.buildTree(inorder[inorder_mid_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_mid_index], postorder)
        return root        
