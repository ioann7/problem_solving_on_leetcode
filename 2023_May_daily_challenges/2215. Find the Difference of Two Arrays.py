# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


# Time complexity O(n). Space complexity O(n).
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_set1 = set(nums1)
        hash_set2 = set(nums2)
        return [list(hash_set1 - hash_set2), list(hash_set2 - hash_set1)]
