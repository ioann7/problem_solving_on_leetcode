# https://leetcode.com/problems/stone-game-iii/

# Time and space complexity O(n).
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @cache
        def dfs(i):
            if i == len(stoneValue):
                return 0
            res = float('-inf')
            for j in range(i, min(i + 3, len(stoneValue))):
                res = max(res, sum(stoneValue[i:j + 1]) - dfs(j + 1))
            return res

        if dfs(0) > 0:
            return 'Alice'
        if dfs(0) < 0:
            return 'Bob'
        return 'Tie'
