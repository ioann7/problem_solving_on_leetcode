# https://leetcode.com/problems/shuffle-the-array/description/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [None] * len(nums)
        left = 0
        right = n
        index = 0
        while left < n and right < len(nums):
            result[index] = nums[left]
            index += 1
            result[index] = nums[right]
            index += 1
            left += 1
            right += 1
        return result
