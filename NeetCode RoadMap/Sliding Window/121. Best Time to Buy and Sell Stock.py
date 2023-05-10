# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        len_prices = len(prices)
        left, right = 0, 1
        while right < len_prices:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
