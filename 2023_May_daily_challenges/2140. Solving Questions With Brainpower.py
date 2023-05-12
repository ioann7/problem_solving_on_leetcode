# https://leetcode.com/problems/solving-questions-with-brainpower/

# Time complexity O(n). Space complexity O(n).
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        for index in range(len(questions) - 1, -1, -1):
            skip = dp[index + 1]
            not_skip = questions[index][0]
            if index + 1 + questions[index][1] < len(questions):
                not_skip = questions[index][0] + dp[index + 1 + questions[index][1]]
            dp[index] = max(skip, not_skip)
        return dp[0]

# recursion method
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int: 

        @cache
        def dfs(index):
            if index >= len(questions):
                return 0
            return max(
                dfs(index + 1),
                questions[index][0] + dfs(index + 1 + questions[index][1])
            )

        return dfs(0)
