# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.search_row_index(matrix, target)
        if row_index == -1:
            return False
        return self.is_target_in_row(matrix[row_index], target)

    def search_row_index(self, matrix: List[List[int]], target: int) -> int:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def is_target_in_row(self, row: List[int], target: int) -> bool:
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False
