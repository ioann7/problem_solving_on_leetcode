# https://leetcode.com/problems/longest-palindromic-substring/

# Time complexity O(n^2). Space complexity O(1).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = (0, 0) # (left, right)
        for index in range(len(s)):
            # odd length
            result = max(
                result,
                self.find_palindrome(index, index, s),
                key=lambda e: e[1] - e[0] + 1
            )
            # even length
            result = max(
                result,
                self.find_palindrome(index, index + 1, s),
                key=lambda e: e[1] - e[0] + 1
            )
        return s[result[0]:result[1] + 1]

    def find_palindrome(self, left: int, right: int, s: str) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # back to last good decision
        left += 1
        right -= 1
        return left, right
