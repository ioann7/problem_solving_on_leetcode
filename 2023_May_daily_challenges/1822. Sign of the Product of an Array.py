# https://leetcode.com/problems/sign-of-the-product-of-an-array/

from typing import List


# Time complexity O(n). Space complexity O(1).
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zero_count = 0
        negative_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num < 0:
                negative_count += 1
        if zero_count:
            return 0
        if negative_count % 2 == 0:
            return 1
        return -1
