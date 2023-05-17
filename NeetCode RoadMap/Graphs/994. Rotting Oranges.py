# https://leetcode.com/problems/rotting-oranges/

# Time complexity O(n*m). Space complexity O(n*m).
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows_count, cols_count = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = set()

        for i in range(rows_count):
            for j in range(cols_count):
                if grid[i][j] == 1:
                    fresh_oranges.add((i, j))
                elif grid[i][j] == 2:
                    queue.append((i, j))

        diffs = ((0, -1), (0, 1), (1, 0), (-1, 0))
        minutes = 0
        while queue:
            if not fresh_oranges:
                return minutes
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for diff in diffs:
                    new_i, new_j = i + diff[0], j + diff[1]
                    if (new_i, new_j) in fresh_oranges:
                        fresh_oranges.remove((new_i, new_j))
                        queue.append((new_i, new_j))
            minutes += 1

        if not fresh_oranges:
            return minutes
        return -1
