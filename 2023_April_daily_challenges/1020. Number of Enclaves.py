# 

from typing import List


# Time complexity is O(rows*cols).
# Space complexity is O(rows*cols) for visit(HashSet) + O(rows*cols) for recursion.
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visit = set()
        result = 0

        def dfs(row, col, land_cells):
            if (row < 0 or row == rows or
                    col < 0 or col == columns):
                return False
            if grid[row][col] == 0 or (row, col) in visit:
                return True
            land_cells[0] += 1
            visit.add((row, col))
            return all((
                dfs(row + 1, col, land_cells),
                dfs(row - 1, col, land_cells),
                dfs(row, col + 1, land_cells),
                dfs(row, col - 1, land_cells),
            ))

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1 and (row, col) not in visit:
                    land_cells = [0]    # this is counter for ones
                    if dfs(row, col, land_cells):
                        result += land_cells[0]
        return result
