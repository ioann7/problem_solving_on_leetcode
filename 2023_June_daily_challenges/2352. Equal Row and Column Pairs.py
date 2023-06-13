# https://leetcode.com/problems/equal-row-and-column-pairs/

# Time complexity O(n*n). Space complexity O(n).
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        result = 0
        for r in range(len(grid)):
            rows[tuple(grid[r])] += 1
        for c in range(len(grid[0])):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            col = tuple(col)
            if col in rows:
                result += rows[col]
        return result
