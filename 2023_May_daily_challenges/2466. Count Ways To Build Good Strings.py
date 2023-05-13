# https://leetcode.com/problems/count-ways-to-build-good-strings/

# Time complexity O(n) because we use caching. Space complexity O(n) for recursive.
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulo = 10**9 + 7

        @cache
        def dfs(length):
            if length > high:
                return 0
            result = 1 if length >= low else 0
            result += dfs(length + zero) + dfs(length + one)
            return result % modulo 

        return dfs(0)
