# https://leetcode.com/problems/house-robber/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_prev, prev = 0, 0
        for num in nums:
            current = max(prev, prev_prev + num)
            prev_prev = prev
            prev = current
        return prev
