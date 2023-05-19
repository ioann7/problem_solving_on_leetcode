# https://leetcode.com/problems/palindromic-substrings/

# Time complexity O(n^2). Space complexity O(1).
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for index in range(len(s)):
            result += self.count_palindrome(index, index, s)
            result += self.count_palindrome(index, index + 1, s)
        return result

    def count_palindrome(self, left: int, right: int, s: str) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
