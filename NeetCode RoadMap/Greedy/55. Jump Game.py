# https://leetcode.com/problems/jump-game/

# Greedy solution. Time complexity O(n). Space complexity O(1).
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_end = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= current_end:
                current_end = index
        return True if current_end == 0 else False


# DP solution. Time complexity O(n^2). Space complexity O(n^2) for caching + recursion.
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        @cache
        def dfs(index):
            if index >= len(nums):
                return False
            if index == len(nums) - 1:
                return True
            for jump in range(min(nums[index], len(nums)), 0, -1):
                if dfs(index + jump):
                    return True
            return False

        return dfs(0)
