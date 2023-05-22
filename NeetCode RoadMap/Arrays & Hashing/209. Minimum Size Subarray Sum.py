# https://leetcode.com/problems/minimum-size-subarray-sum/

# Time complexity O(n). Space complexity (1).
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        cur_sum = 0
        left = 0
        for right, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                min_length = min(min_length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
