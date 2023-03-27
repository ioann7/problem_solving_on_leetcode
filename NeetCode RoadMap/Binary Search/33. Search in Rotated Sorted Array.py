# https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return -1
        return -1


# My first solution. Using recursion but here i make unnecessary actions
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums: List[int], left: int,
                      right: int, target: int) -> int:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if right - left < 1:
            return -1
        if nums[left] > nums[right]:
            left_bs = self.binary_search(nums, left, mid - 1, target)
            right_bs = self.binary_search(nums, mid + 1, right, target)
            return max(left_bs, right_bs)
        elif target < nums[mid]:
            return self.binary_search(nums, left, mid - 1, target)
        elif target > nums[mid]:
            return self.binary_search(nums, mid + 1, right, target)
