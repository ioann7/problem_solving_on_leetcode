# https://leetcode.com/problems/spiral-matrix/

# Time complexity O(n*m). Space complexity O(1).
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_row, right_row = 0, len(matrix) - 1
        left_col, right_col = 0, len(matrix[0]) - 1
        index = 0
        result = [None] * (len(matrix) * len(matrix[0]))
        while left_col <= right_col and left_row <= right_row:
            for col in range(left_col, right_col + 1):
                result[index] = matrix[left_row][col]
                index += 1
            left_row += 1
            for row in range(left_row, right_row + 1):
                result[index] = matrix[row][right_col]
                index += 1
            right_col -= 1
            if index == len(result):
                return result
            for col in range(right_col, left_col - 1, -1):
                result[index] = matrix[right_row][col]
                index += 1
            right_row -= 1
            for row in range(right_row, left_row - 1, -1):
                result[index] = matrix[row][left_col]
                index += 1
            left_col += 1
        return result
