# https://leetcode.com/problems/3sum

from typing import List


# Time complexity: sorting O(n*log(n)) + O(n^2) = O(n^2). Space complexity O(1) or O(n) for sorting.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            target = -nums[index]
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result


# My first solution.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for left, num in enumerate(nums[:-2]):
            target = -num
            nums_dict = {}
            right = left + 1
            while right < len(nums):
                if (target - nums[right]) in nums_dict:
                    result.add(
                        tuple(sorted((
                            num,
                            nums[nums_dict[target - nums[right]]],
                            nums[right]
                        )))
                    )
                nums_dict[nums[right]] = right
                right += 1
        return list(result)
