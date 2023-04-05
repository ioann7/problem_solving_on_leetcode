# https://leetcode.com/problems/minimize-maximum-of-array

from typing import List


# Time complexity O(N). Space complexity O(1).
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        current_sum = nums[0]
        for index in range(1, len(nums)):
            current_sum = current_sum + nums[index]
            result = max(result, math.ceil(current_sum / (index + 1)))
        return result
