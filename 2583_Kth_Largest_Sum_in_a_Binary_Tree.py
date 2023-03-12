# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_values = defaultdict(list)

        def direct_travelsal(root: Optional[TreeNode], level: int = 0) -> None:
            if root is None:
                return
            level_values[level].append(root.val)
            direct_travelsal(root.left, level + 1)
            direct_travelsal(root.right, level + 1)

        direct_travelsal(root)
        if len(level_values) < k:
            return -1
        return sorted(map(sum, level_values.values()))[-k]
