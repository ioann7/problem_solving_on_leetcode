# https://leetcode.com/problems/two-sum/


from typing imort List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for current_index, num in enumerate(nums):
            if (target - num) in nums_dict:
                return nums_dict[(target - num)], current_index
            nums_dict[num] = current_index
