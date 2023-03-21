# https://leetcode.com/problems/maximize-distance-to-closest-person/description/

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        result = 0
        start_zero = 0
        # edge case for start
        while seats[start_zero] == 0:
            start_zero += 1
            result = max(result, start_zero)
        for index in range(start_zero, len(seats)):
            if seats[index] != 0:
                start_zero = index + 1
            result = max(result, (index - start_zero + 2) // 2)
        # edge case for end
        result = max(result, index - start_zero + 1)
        return result
