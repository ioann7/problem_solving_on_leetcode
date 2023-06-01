# Time and space O(n^2) because n x n matrix. 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        queue = deque([(0, 0)])
        length = 1
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0),
                     (1, 1), (-1, -1), (-1, 1), (1, -1)]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for dr, dc in neighbors:
                    is_out_of_bounds_or_visited = any((
                        min(row + dr, col + dc) < 0,
                        row + dr == ROWS,
                        col + dc == COLS,
                        (row + dr, col + dc) in visit,
                    ))
                    if not (is_out_of_bounds_or_visited or grid[row + dr][col + dc] == 1):
                        visit.add((row + dr, col + dc))
                        queue.append((row + dr, col + dc))
            length += 1
        return -1
