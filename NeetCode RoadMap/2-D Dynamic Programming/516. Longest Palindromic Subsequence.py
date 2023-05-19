# https://leetcode.com/problems/longest-palindromic-subsequence/

# Time and space O(n^2).
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dfs(start: int, end: int) -> int:
            if start == end:
                return 1
            if start > end:
                return 0
            if s[start] == s[end]:
                return 2 + dfs(start + 1, end - 1)
            return max(dfs(start + 1, end), dfs(start, end - 1))

        return dfs(0, len(s) - 1)


# Cheat code ;)) i am already solve this question here: 1143. Longest Common Subsequence
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, list(reversed(s)))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        dp = [[0] * cols for _ in range(rows)]
        for row in reversed(range(rows - 1)):
            for col in reversed(range(cols - 1)):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(
                        dp[row + 1][col],
                        dp[row][col + 1]
                    )
        return dp[0][0]
