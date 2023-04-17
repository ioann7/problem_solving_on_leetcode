# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List


# Time complexity O(n). Space complexity O(n), just for answer.
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return map(lambda item: (item + extraCandies) >= max(candies), candies)


# Faster solution.
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        is_greatest = lambda item: (item + extraCandies) >= max_candy
        return [True if is_greatest(item) else False for item in candies]
