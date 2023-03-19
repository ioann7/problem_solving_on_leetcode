# https://leetcode.com/problems/remove-element/description/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


# another way
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        k = len(nums)
        while left <= right:
            if nums[right] == val:
                right -= 1
                k -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                right -= 1
                k -= 1
                left += 1
            else:
                left += 1
        return k
