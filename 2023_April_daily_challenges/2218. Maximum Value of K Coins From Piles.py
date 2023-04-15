# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @functools.cache
        def dfs(index, coins):
            if index == len(piles):
                return 0
            result = dfs(index + 1, coins)
            cur_pile = 0
            for j in range(min(coins, len(piles[index]))):
                cur_pile += piles[index][j]
                result = max(
                    result, cur_pile + dfs(index + 1, coins - j - 1)
                )
            return result

        return dfs(0, k)
