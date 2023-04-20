# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time complexity is O(n) where n is nodes. Space complexity O(n) for recusrive.
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        result = 0

        def lmr(node: TreeNode, from_edge: str, zigzag_length: int) -> None:
            nonlocal result
            if node.left:
                if from_edge == 'right':
                    lmr(node.left, 'left', zigzag_length + 1)
                else:
                    lmr(node.left, 'left', 1)
            if node.right:
                if from_edge == 'left':
                    lmr(node.right, 'right', zigzag_length + 1)
                else:
                    lmr(node.right, 'right', 1)
            result = max(result, zigzag_length)

        if root.left:
            lmr(root.left, 'left', 1)
        if root.right:
            lmr(root.right, 'right', 1)
        return result
