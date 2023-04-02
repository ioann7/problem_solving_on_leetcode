# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

from typing import List


# Time complexity: for sorting O(M * logM) and solution O(N * logM) = O((N+M)logM). Space complexity: O(N) for result.
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = [None] * len(spells)
        potions.sort()
        for index, spell in enumerate(spells):
            pairs = len(potions) - self.binary_search(potions, self.ceildiv(success, spell))
            result[index] = pairs
        return result

    def ceildiv(self, a: int, b: int):
        return -(a // -b)

    def binary_search(self, values: List[int], target: int) -> int:
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
