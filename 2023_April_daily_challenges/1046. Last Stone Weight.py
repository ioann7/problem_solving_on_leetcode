# https://leetcode.com/problems/last-stone-weight/

from typing import List


# Time complexity O(n*log(n)). Space complexity O(n).
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                stone1, stone2 = sorted((stone1, stone2))
                heapq.heappush(stones, stone1 - stone2)
        if stones:
            return -stones[0]
        return 0
