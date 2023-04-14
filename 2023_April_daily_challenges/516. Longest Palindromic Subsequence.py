# Time complexity O(n^2). Space complexity O(n^2). But this solution is time limit exceeded.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(i, j):
            is_out_of_bounds = i < 0 or j == len(s)
            if is_out_of_bounds:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if s[i] == s[j]:
                length = 1 if i == j else 2
                length = length + dfs(i - 1, j + 1)
                cache[(i, j)] = length
            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        result = 0
        for index in range(len(s)):
            odd = dfs(index, index)
            even = dfs(index, index + 1)
            result = max(result, odd, even)
        return result


# This is solution without limit exceeded, but less readable. Time and Space comp the same.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        res = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res
