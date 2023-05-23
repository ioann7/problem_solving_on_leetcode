# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows_count, cols_count = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (cols_count + 1) for _ in range(rows_count + 1)]
        for r in range(rows_count):
            prefix = 0
            for c in range(cols_count):
                prefix += matrix[r][c]
                above = self.prefix_sum[r][c + 1]
                self.prefix_sum[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        right_bottom = self.prefix_sum[row2][col2]
        above = self.prefix_sum[row1 - 1][col2]
        left = self.prefix_sum[row2][col1 - 1]
        intersection = self.prefix_sum[row1 - 1][col1 - 1]
        return right_bottom - above - left + intersection


"""
Представим что, запрос obj.sumRegion(row1=1, col1=1, row2=4, col2=4).
Тогда мне нужно найти полный квадрат от row1=0, col1=0, row2=4, col2=4
затем вычесть верхний и левый прямоугольник, а там прибавить то пересечение, что я вычел дважды
то есть: верхний прямоугольник row=0, col=4
а левый прямоугольник row=4, col=0
и теперь прибавить пересечение row=0, col=0
 _______
|_|_|_|_|
|_|_|_|_|
|_|_|_|_|
|_|_|_|_|
"""
