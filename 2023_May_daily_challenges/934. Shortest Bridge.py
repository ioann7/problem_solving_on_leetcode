# https://leetcode.com/problems/shortest-bridge/

# Time complexity O(n^2). Space complexity O(n^2).
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row = 0
        col = 0
        # find first one's
        while row < rows and col < cols and grid[row][col] != 1:
            col += 1
            if col == cols:
                col = 0
                row += 1

        # add first island in visit
        visit = set()
        queue = deque(((row, col),))
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if ((row, col) in visit or min(row, col) < 0
                        or row == rows or col == cols):
                    continue
                if grid[row][col] == 1:
                    visit.add((row, col))
                    queue.extend(((row - 1, col), (row + 1, col),
                                  (row, col - 1), (row, col + 1)))

        # run bfs for search shortest path between 2 islands
        queue = deque()
        for (row, col) in visit:
            queue.extend(((row - 1, col), (row + 1, col),
                          (row, col - 1), (row, col + 1)))
        length = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if ((row, col) in visit or min(row, col) < 0
                        or row == rows or col == cols):
                    continue
                if grid[row][col] == 0:
                    visit.add((row, col))
                    queue.extend(((row - 1, col), (row + 1, col),
                                    (row, col - 1), (row, col + 1)))
                else:
                    return length
            length += 1
