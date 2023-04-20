# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        self.lmr(root, result)
        return result

    def lmr(self, root: TreeNode, to_save: List[int]) -> None:
        if root.left:
            self.lmr(root.left, to_save)
        to_save.append(root.val)
        if root.right:
            self.lmr(root.right, to_save)
