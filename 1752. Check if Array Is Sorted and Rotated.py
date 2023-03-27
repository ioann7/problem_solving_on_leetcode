# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        index = 1
        while index < len(nums) and nums[index] >= nums[index - 1]:
            index += 1
        if index == len(nums):
            return True
        index += 1
        while index < len(nums) and nums[index] >= nums[index - 1]:
            index += 1
        if index == len(nums) and nums[-1] <= nums[0]:
            return True
        return False
