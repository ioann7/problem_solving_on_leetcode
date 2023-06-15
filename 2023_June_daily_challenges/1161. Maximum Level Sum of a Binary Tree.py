# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        max_sum_level = 0
        while queue:
            cur_sum = 0
            for _ in range(len(queue)):
                val = queue.popleft()
                cur_sum += val.val
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
            if max_sum < cur_sum:
                max_sum = cur_sum
                max_sum_level = level
            level += 1
        return max_sum_level
