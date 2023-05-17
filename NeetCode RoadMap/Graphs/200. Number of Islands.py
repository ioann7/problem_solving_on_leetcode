# https://leetcode.com/problems/number-of-islands/

# Time complexity O(n*m). Space complexity O(n*m).
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(i, j):
            is_out_of_bounds_or_visited = any((
                (i, j) in visit,
                min(i, j) < 0,
                i == ROWS,
                j == COLS,
            ))
            if is_out_of_bounds_or_visited or grid[i][j] == '0':
                return
            visit.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit and grid[row][col] == '1':
                    dfs(row, col)
                    result += 1
        return result
