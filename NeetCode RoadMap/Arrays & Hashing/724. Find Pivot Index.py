# https://leetcode.com/problems/find-pivot-index/

# Time and Space complexity is O(n).
class Solution:
    def runningSum(self, nums: List[int], count: Optional[int] = None) -> List[int]:
        count = count or len(nums)
        result = [None] * count
        prev_num = 0
        for index, num in enumerate(nums):
            prev_num += num
            result[index] = prev_num
        return result

    def pivotIndex(self, nums: List[int]) -> int:
        count = len(nums)
        left = self.runningSum(nums, count)
        right = self.runningSum(reversed(nums), count)
        for index in range(count):
            if left[index] == right[-index - 1]:
                return index
        return -1
