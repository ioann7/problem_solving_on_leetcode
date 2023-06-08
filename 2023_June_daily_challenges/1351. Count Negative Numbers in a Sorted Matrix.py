# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# Time comlexity O(n + m). Space complexity O(1).
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        start = 0
        for row in reversed(range(ROWS)):
            start = bisect_right(grid[row], 0, key=lambda e: -e, lo=start)
            negative_count = COLS - start
            result += negative_count
        return result
