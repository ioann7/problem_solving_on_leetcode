# https://leetcode.com/problems/concatenation-of-array/

# Time complexity O(n). Space complexity O(n) for result
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_capacity = (len(nums) * 2)
        result = [None] * new_capacity
        for index in range(new_capacity):
            result[index] = nums[index % len(nums)]
        return result
