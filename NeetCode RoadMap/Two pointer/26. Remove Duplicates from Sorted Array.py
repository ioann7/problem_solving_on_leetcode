# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        current_value = nums[0]
        paste_index = 1
        index = 1
        while index < len(nums):
            if nums[index] != current_value:
                current_value = nums[index]
                nums[paste_index] = current_value
                paste_index += 1
            index += 1
        return paste_index
