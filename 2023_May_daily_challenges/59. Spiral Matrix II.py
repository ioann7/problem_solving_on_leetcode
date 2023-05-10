# Time complexity O(n^2) because we build matrix n * n. Space complexity O(n^2) because we build that matrix.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left_row, right_row = 0, n - 1
        left_col, right_col = 0, n - 1
        value = 1
        matrix = [[None] * n for _ in range(n)]
        while left_col <= right_col and left_row <= right_row:
            for col in range(left_col, right_col + 1):
                matrix[left_row][col] = value
                value += 1
            left_row += 1
            for row in range(left_row, right_row + 1):
                matrix[row][right_col] = value
                value += 1
            right_col -= 1
            if value > n * n:
                return matrix
            for col in range(right_col, left_col - 1, -1):
                matrix[right_row][col] = value
                value += 1
            right_row -= 1
            for row in range(right_row, left_row - 1, -1):
                matrix[row][left_col] = value
                value += 1
            left_col += 1
        return matrix
