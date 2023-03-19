# https://leetcode.com/problems/summary-ranges


from typing import List


class Solution:
    def appendResult(self, start: int, end: int, result: List[str]) -> None:
        if start == end:
            result.append(str(start))
        else:
            result.append(f'{start}->{end}')

    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        start = nums[0]
        index = 1
        while index < len(nums):
            if nums[index] - nums[index - 1] > 1:
                self.appendResult(start, nums[index - 1], result)
                start = nums[index]
            index += 1
        self.appendResult(start, nums[index - 1], result)
        return result
