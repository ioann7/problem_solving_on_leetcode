# https://leetcode.com/problems/unique-paths-ii/

# Time and Space complexity O(n*m)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * cols
        prev_row[-1] = 1
        for row in range(rows - 1, -1, -1):
            cur_row = [0] * cols
            if obstacleGrid[row][-1] == 0:
                cur_row[-1] = prev_row[-1]
            for col in range(cols - 2, -1, -1):
                if obstacleGrid[row][col] == 0:
                    cur_row[col] = cur_row[col + 1] + prev_row[col]
            prev_row = cur_row
        return prev_row[0]
