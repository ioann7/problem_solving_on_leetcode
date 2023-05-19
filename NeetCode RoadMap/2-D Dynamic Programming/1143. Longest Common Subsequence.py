# https://leetcode.com/problems/longest-common-subsequence/

# Time and space complexity O(n*m).
class Solution:
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
