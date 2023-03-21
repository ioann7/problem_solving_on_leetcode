from typing import List


class Solution:
    def zero_filled_subarray(self, nums: List[int]) -> int:
        result = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                right += 1
                left = right
            elif nums[right] == 0:
                current_zeros_len = right - left + 1
                result += current_zeros_len
                right += 1
        return result


# after refactoring
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        start_zeros = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                start_zeros = index + 1
            result += index - start_zeros + 1
        return result
