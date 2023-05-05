# https://leetcode.com/problems/max-area-of-island/

# Time complexity O(n*m). Space complexity O(n*m) for visit.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(i, j, cur_area):
            is_out_of_bounds_or_visited = any((
                min(i, j) < 0,
                i == ROWS,
                j == COLS,
                (i, j) in visit,
            ))
            if is_out_of_bounds_or_visited or grid[i][j] == 0:
                return 0
            visit.add((i, j))
            cur_area += 1
            cur_area = max(cur_area, dfs(i + 1, j, cur_area))
            cur_area = max(cur_area, dfs(i - 1, j, cur_area))
            cur_area = max(cur_area, dfs(i, j + 1, cur_area))
            cur_area = max(cur_area, dfs(i, j - 1, cur_area))
            return cur_area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visit:
                    max_area = max(max_area, dfs(row, col, 0))
        return max_area
