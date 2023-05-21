# https://leetcode.com/problems/valid-sudoku/

# Time complexity O(9*9) = O(n^2). Space complexity O(3*9*9)=O(3*n^2).
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_size = 9
        rows = [set() for _ in range(sudoku_size)]
        cols = [set() for _ in range(sudoku_size)]
        boxes = [set() for _ in range(sudoku_size)]
        for row in range(sudoku_size):
            for col in range(sudoku_size):
                cur_value = board[row][col]
                if cur_value != '.':
                    box = ((row // 3) * 3) + (col // 3)
                    is_repetition = any((
                        cur_value in rows[row],
                        cur_value in cols[col],
                        cur_value in boxes[box],
                    ))
                    if is_repetition:
                        return False
                    rows[row].add(cur_value)
                    cols[col].add(cur_value)
                    boxes[box].add(cur_value)
        return True
