# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] and nums[left] <= nums[right]:
                return nums[left]
            elif nums[right] <= nums[mid] and nums[right] <= nums[left]:
                left = mid + 1
            else:
                right = mid
