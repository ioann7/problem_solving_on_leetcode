# https://leetcode.com/problems/longest-consecutive-sequence/

# Time and memory complexity is O(n).
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums_set = set(nums)
        for num in nums:
            if num not in nums_set:
                continue
            nums_set.remove(num)
            consecutive = 1
            left_num = num - 1
            while left_num in nums_set:
                nums_set.remove(left_num)
                consecutive += 1
                left_num -= 1
            right_num = num + 1
            while right_num in nums_set:
                nums_set.remove(right_num)
                consecutive += 1
                right_num += 1
            result = max(result, consecutive)
        return result
