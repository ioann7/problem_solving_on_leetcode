# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def lmr(root):
            if root.left:
                lmr(root.left)
            values.append(root.val)
            if root.right:
                lmr(root.right)

        lmr(root)
        return min([val2 - val1 for val1, val2 in zip(values, values[1:])])
