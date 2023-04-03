# https://leetcode.com/problems/boats-to-save-people

from typing import List


# Time complexity is O(N*logN) because we are sorting array. Space complexity O(1).
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
