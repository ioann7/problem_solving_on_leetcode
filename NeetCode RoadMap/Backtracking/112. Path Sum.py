# https://leetcode.com/problems/path-sum/

# time comp O(n). space comp O(1)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        current_target_sum = targetSum - root.val
        if not root.left and not root.right and current_target_sum == 0:
            return True
        if self.hasPathSum(root.left, current_target_sum):
            return True
        if self.hasPathSum(root.right, current_target_sum):
            return True
        return False
