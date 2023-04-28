# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

from typing import List


# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        left = 0
        for right in range(1, len(prices)):
            if prices[right] <= prices[left]:
                left = right
            elif right + 1 == len(prices) or prices[right + 1] < prices[right]:
                total += prices[right] - prices[left]
                left = right + 1
        return total
