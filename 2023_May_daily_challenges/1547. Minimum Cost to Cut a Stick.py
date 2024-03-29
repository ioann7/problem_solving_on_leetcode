# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def dfs(l, r):
            if r - l == 1:
                return 0
            res = float('inf')
            for c in cuts:
                if l < c < r:
                    res = min(
                        res,
                        (r - l) + dfs(l, c) + dfs(c, r)
                    )
            return 0 if res == float('inf') else res

        return dfs(0, n)
