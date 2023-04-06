# https://leetcode.com/problems/number-of-closed-islands/

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, col: int) -> bool:
            if (row < 0 or row >= rows or
                    col < 0 or col >= columns):
                return False
            if (row, col) in visited or grid[row][col] == 1:
                return True
            visited.add((row, col))
            return all((
                dfs(row + 1, col),
                dfs(row - 1, col),
                dfs(row, col + 1),
                dfs(row, col - 1),
            ))

        result = 0
        for row in range(rows):
            for col in range(columns):
                if (row, col) not in visited and grid[row][col] == 0:
                    result += dfs(row, col)
        return result
