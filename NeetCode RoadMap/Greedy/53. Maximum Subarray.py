# https://leetcode.com/problems/maximum-subarray/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum
