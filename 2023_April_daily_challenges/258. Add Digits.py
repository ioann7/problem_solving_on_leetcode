# https://leetcode.com/problems/add-digits/

# Time complexity O(1). Space complexity O(1).
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        result = num % 9
        if result == 0:
            result = 9
        return result
