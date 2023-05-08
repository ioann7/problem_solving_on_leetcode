# Time complexity O(n). Space complexity O(1).
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for index1, index2 in zip(range(len(mat)), range(len(mat) - 1, -1, -1)):
            result += mat[index1][index1]
            result += mat[index1][index2]
        if len(mat) % 2 == 1:
            result -= mat[len(mat) // 2][len(mat) // 2]
        return result
