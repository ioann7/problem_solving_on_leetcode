# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# Time complexity O(nlogn) for sorting + O(n) for solution. Space complexity O(1).
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        modulo = 10**9 + 7
        result = 0
        right = len(nums) - 1
        for left, value in enumerate(nums):
            while (value + nums[right]) > target and left <= right:
                right -= 1
            if left <= right:
                result += 2**(right - left)
                result %= modulo
        return result
