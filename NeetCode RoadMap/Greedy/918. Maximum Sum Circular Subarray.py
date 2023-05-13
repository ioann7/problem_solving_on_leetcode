# https://leetcode.com/problems/maximum-sum-circular-subarray/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min = nums[0]
        global_max = nums[0]
        cur_min = 0
        cur_max = 0
        for num in nums:
            cur_min = min(cur_min, 0)
            cur_min += num
            global_min = min(global_min, cur_min)
            cur_max = max(cur_max, 0)
            cur_max += num
            global_max = max(global_max, cur_max)
        if global_max < 0:
            return global_max
        return max(global_max, sum(nums) - global_min)
