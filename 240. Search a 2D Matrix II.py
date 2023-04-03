# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


# Time complexity is O(N + M). Space complexity O(1).
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        row = n - 1
        column = 0
        while row >= 0 and column < m:
            if matrix[row][column] == target:
                return True
            if matrix[row][column] > target:
                row -= 1
            else:
                column += 1
        return False
