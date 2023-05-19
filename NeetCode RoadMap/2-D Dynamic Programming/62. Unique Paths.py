# https://leetcode.com/problems/unique-paths/

# Time and Space complexity O(n*m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n
        for _ in range(m):
            cur_row = [0] * n
            cur_row[-1] = 1
            for col in range(n - 2, -1, -1):
                cur_row[col] = cur_row[col + 1] + prev_row[col]
            prev_row = cur_row
        return prev_row[0]
